import re
import collections
import json

from kraken.core.objects.components.base_example_component import BaseExampleComponent
from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.joint import Joint
from kraken.core.objects.locator import Locator
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.maths import *

# What?  Why do I have do this?  Not even in Maya.  Fabric F'ed something up with rotation orders.
ROT_ORDER_REMAP = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 0,
    5: 2
}


def clamp(value, min_value, max_value):
        return max(min(value, max_value), min_value)

def min_scale(value, threshold=0.0001):
    if abs(value) < threshold:
        value = threshold

    if abs(1- value) < threshold:
        value = 1.0

    return value

def min_thresh(value, threshold=0.0001):
    if abs(value) < threshold:
        return 0
    return value

def export_glue_json(builder, filepath):

    jdict = collections.OrderedDict()
    jdict["clipType"] = "KrakenGlueClip"

    constraint_dict_src = collections.OrderedDict([
        #"M_root_fk": {"joint":"M_root_def"},
        ("M_cog_fk", {"joint": "M_pelvis_def", "spaceJoint": "world"}),
        ("M_torso_fk", {"joint": "M_spine01_def", "spaceJoint": "M_pelvis_def"}),
        ("M_chest_fk", {"joint": "M_spine03_def", "spaceJoint": "M_spine01_def"}),
        ("M_upChest_fk", {"joint": "M_spine05_def", "spaceJoint": "M_spine03_def"}),
        ("M_neck_fk", {"joint": "M_neck01_def", "spaceJoint": "M_spine05_def"}),
        ("M_head_fk", {"joint": "M_head_def", "spaceJoint": "M_neck01_def"}),
        ("SIDE_upLeg_fk", {"joint": "SIDE_upLeg_def", "spaceJoint": "M_pelvis_def"}),
        ("SIDE_loLeg_fk", {"joint": "SIDE_loLeg_def", "spaceJoint": "SIDE_upLeg_def"}),
        ("SIDE_foot_fk", {"joint": "SIDE_foot_def", "spaceJoint": "SIDE_loLeg_def"}),
        ("SIDE_ball_fk", {"joint": "SIDE_ball_def", "spaceJoint": "SIDE_foot_def"}),
        ("SIDE_shldr_fk", {"joint": "SIDE_shldr_def", "spaceJoint": "M_spine05_def"}),
        ("SIDE_upArm_fk", {"joint": "SIDE_upArm_def", "spaceJoint": "SIDE_shldr_def"}),
        ("SIDE_loArm_fk", {"joint": "SIDE_loArm_def", "spaceJoint": "SIDE_upArm_def"}),
        ("SIDE_hand_fk", {"joint": "SIDE_hand_def", "spaceJoint": "SIDE_loArm_def"})
        ])

    segments = ["palm", "base", "mid", "tip"]
    for finger in ["thumb", "index", "middle", "ring", "pinky"]:
        for i, segment in enumerate(segments):  # ["palm", "base", "mid", "tip"]

            if finger+"_"+segment == "thumb_mid":
                continue
            if finger+"_"+segment == "thumb_tip":
                i = i-1

            fk = "SIDE_"+finger+"_"+segment+"_fk"
            finger_dict = dict()
            finger_dict["joint"] = fk.replace("_fk", "_def")
            if i == 0:
                finger_dict["spaceJoint"] = "SIDE_hand_def"
            else:
                finger_dict["spaceJoint"] = "SIDE_"+finger+"_"+segments[i-1]+"_def"

            constraint_dict_src[fk] = finger_dict


    constraint_dict = collections.OrderedDict()

    for ctrl, data in constraint_dict_src.iteritems():
        if "SIDE" in ctrl:
            for side in ["L", "R"]:
                dupdata = data.copy()
                for key, value in dupdata.iteritems():
                    dupdata[key] = value.replace("SIDE", side)
                constraint_dict[ctrl.replace("SIDE", side)] = dupdata
        else:
            constraint_dict[ctrl] = data


    objects = {o['sceneItem'].getBuildName():o['sceneItem'] for o in builder._Builder__klObjects}
    for kconstraint in [c['sceneItem'] for c in builder._Builder__klConstraints]:
        kconstraint.evaluate() #Make sure all leaf nodes are evaluated

    def make_constraint(object3D, joint, space=None):
        spacestr = " (space = %s)" % space if space else ""
        print("    Making glue constraint: object3D[%s] to joint[%s]%s" % (object3D, joint, spacestr))

        constraint = collections.OrderedDict()
        constraint["object3D"] = object3D
        constraint["joint"] = joint
        if space:
            constraint["space"] = space

        if joint in objects.keys():
            offset = objects[joint].xfo.inverse() * objects[object3D].xfo
        else:
            offset = objects[object3D].xfo

        constraint["tOffset"] = collections.OrderedDict([
            ("x", min_thresh(offset.tr.x)),
            ("y", min_thresh(offset.tr.y)),
            ("z", min_thresh(offset.tr.z))
            ])

        euler = offset.ori.toEuler(objects[object3D].ro)
        constraint["rOffset"] = collections.OrderedDict([
            ("x", min_thresh(Math_radToDeg(euler.x))),
            ("y", min_thresh(Math_radToDeg(euler.y))),
            ("z", min_thresh(Math_radToDeg(euler.z)))
            ])
        constraint["order"] = ROT_ORDER_REMAP[objects[object3D].ro.order]

        constraint["sOffset"] = collections.OrderedDict([
            ("x", min_scale(offset.sc.x)),
            ("y", min_scale(offset.sc.y)),
            ("z", min_scale(offset.sc.z))
            ])

        return constraint


    constraints = list()

    for ctrl, data in constraint_dict.iteritems():

        if ctrl not in objects.keys():
            raise Exception("Ctrl [%s] not found in object list %s" % (ctrl, "\n".join(objects.keys())))
        if data["joint"] not in objects.keys():
            raise Exception("Joint [%s] not found in deformer list %s" % (data["joint"], "\n".join(objects.keys())))

        if data["spaceJoint"] not in objects.keys() and data["spaceJoint"].lower() != "world":
            raise Exception("spaceJoint [%s] not found in deformer list %s" % (data["spaceJoint"], "\n".join(objects.keys())))

        space = objects[ctrl].getParent().getBuildName()
        constraints.append(make_constraint(space, data["spaceJoint"]))
        constraints.append(make_constraint(ctrl, data["joint"], space=space))

    jdict["content"] = {"constraints": constraints}

    with open(filepath, 'w') as fp:
        json.dump(jdict, fp, sort_keys=False, indent=4)
        print("\nSaved %s\n" % filepath)





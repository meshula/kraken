
import unittest

from attributes import suite as attributeSuite
from components import suite as componentSuite
from constraints import suite as constraintSuite
from operators import suite as operatorSuite

from test_component_group import suite as componentGroupSuite
from test_container import suite as containerSuite
from test_control import suite as controlSuite
from test_ctrlSpace import suite as ctrlSpaceSuite
from test_curve import suite as curveSuite
from test_hierarchy_group import suite as hierarchyGroupSuite
from test_joint import suite as jointSuite
from test_layer import suite as layerSuite
from test_locator import suite as locatorSuite
from test_object_3d import suite as object3DSuite
from test_rig import suite as rigSuite
from test_scene_item import suite as sceneItemSuite
from test_transform import suite as transformSuite

loadAttributeSuite = attributeSuite()
loadComponentSuite = componentSuite()
loadConstraintSuite = constraintSuite()
loadOperatorSuite = operatorSuite()

loadComponentGroupSuite = componentGroupSuite()
loadContainerSuite = containerSuite()
loadControlSuite = controlSuite()
loadCtrlSpaceSuite = ctrlSpaceSuite()
loadCurveSuite = curveSuite()
loadHierarchyGroupSuite = hierarchyGroupSuite()
loadJointSuite = jointSuite()
loadLayerSuite = layerSuite()
loadLocatorSuite = locatorSuite()
loadObject3DSuite = object3DSuite()
loadRigSuite = rigSuite()
loadSceneItemSuite = sceneItemSuite()
loadTransformSuite = transformSuite()


def suite():
    suites = [
        loadAttributeSuite,
        loadComponentSuite,
        loadConstraintSuite,
        loadOperatorSuite,
        loadContainerSuite,
        loadControlSuite,
        loadCtrlSpaceSuite,
        loadCurveSuite,
        loadHierarchyGroupSuite,
        loadJointSuite,
        loadLayerSuite,
        loadLocatorSuite,
        loadObject3DSuite,
        loadRigSuite,
        loadSceneItemSuite,
        loadTransformSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

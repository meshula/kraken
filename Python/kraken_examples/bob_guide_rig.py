from kraken.core.maths import Vec3, Quat, Xfo, Math_degToRad

from kraken.core.objects.rig import Rig

from kraken_components.generic.mainSrt_component import MainSrtComponentGuide
from kraken_components.biped.spine_component import SpineComponentGuide
from kraken_components.biped.neck_component import NeckComponentGuide
from kraken_components.biped.head_component import HeadComponentGuide
from kraken_components.biped.leg_component import LegComponentGuide
from kraken_components.biped.foot_component import FootComponentGuide
from kraken_components.biped.clavicle_component import ClavicleComponentGuide
from kraken_components.biped.arm_component import ArmComponentGuide
from kraken_components.biped.hand_component import HandComponentGuide

from kraken.core.profiler import Profiler


class BobGuideRig(Rig):
    """Bob guide rig.

    This guide is loaded with setting for each component that line up with the
    Bob sample geometry provided within the Resources directory of main Kraken
    directory."""

    def __init__(self, name):

        Profiler.getInstance().push("Construct BobGuideRig:" + name)
        super(BobGuideRig, self).__init__(name)

        # ===========
        # Components
        # ===========
        mainSrtComponentGuide = MainSrtComponentGuide('mainSrt', parent=self)
        spineComponentGuide = SpineComponentGuide('spine', parent=self)
        neckComponentGuide = NeckComponentGuide('neck', parent=self)
        headComponentGuide = HeadComponentGuide('head', parent=self)

        clavicleLeftComponentGuide = ClavicleComponentGuide('clavicle', parent=self)
        clavicleRightComponentGuide = ClavicleComponentGuide('clavicle', parent=self)
        clavicleRightComponentGuide.loadData({
            "name": 'clavicle',
            "location": 'R',
            "clavicleXfo": Xfo(Vec3(-0.15, 15.5, -0.5)),
            "clavicleUpVXfo": Xfo(Vec3(-0.15, 16.5, -0.5)),
            "clavicleEndXfo": Xfo(Vec3(-2.25, 15.5, -0.75))
        })


        armLeftComponentGuide = ArmComponentGuide('arm', parent=self)
        armRightComponentGuide = ArmComponentGuide('arm', parent=self)
        armRightComponentGuide.loadData({
            "name": 'arm',
            "location": 'R',
            "bicepXfo": Xfo(Vec3(-2.275, 15.3, -0.75)),
            "forearmXfo": Xfo(Vec3(-5.0, 13.5, -0.75)),
            "wristXfo": Xfo(Vec3(-7.2, 12.25, 0.5)),
            "bicepFKCtrlSize": 1.75,
            "forearmFKCtrlSize": 1.5
        })

        handLeftComponentGuide = HandComponentGuide('hand', parent=self)
        handRightComponentGuide = HandComponentGuide('hand', parent=self)

        handRightOri = Quat()
        handRightOri.setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(180))

        handRightComponentGuide.loadData({
            "name": 'hand',
            "location": 'R',
            "handXfo": Xfo(tr=Vec3(-7.1886, 12.2819, 0.4906), ori=handRightOri),
            "digitNames": "thumb,index,middle,ring,pinky",
            "numJoints": 4,
            "fingersGuideXfos": {
                "pinky": [
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.439000129699707, y=12.281900405883789, z=0.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.814000129699707, y=12.281900405883789, z=0.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.064000129699707, y=12.281900405883789, z=0.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.314000129699707, y=12.281900405883789, z=0.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.564000129699707, y=12.281900405883789, z=0.0),
                        ori=handRightOri)
                ],
                "index": [
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.439000129699707, y=12.281900405883789, z=0.75),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.814000129699707, y=12.281900405883789, z=0.75),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.064000129699707, y=12.281900405883789, z=0.75),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.314000129699707, y=12.281900405883789, z=0.75),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.564000129699707, y=12.281900405883789, z=0.75),
                        ori=handRightOri)
                ],
                "ring": [
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.439000129699707, y=12.281900405883789, z=0.25),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.814000129699707, y=12.281900405883789, z=0.25),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.064000129699707, y=12.281900405883789, z=0.25),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.314000129699707, y=12.281900405883789, z=0.25),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.564000129699707, y=12.281900405883789, z=0.25),
                        ori=handRightOri)
                ],
                "thumb": [
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.439000129699707, y=12.281900405883789, z=1.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.814000129699707, y=12.281900405883789, z=1.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.064000129699707, y=12.281900405883789, z=1.0),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.314000129699707, y=12.281900405883789, z=1.0),
                        ori=handRightOri)
                ],
                "middle": [
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.439000129699707, y=12.281900405883789, z=0.5),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-7.814000129699707, y=12.281900405883789, z=0.5),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.064000129699707, y=12.281900405883789, z=0.5),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.314000129699707, y=12.281900405883789, z=0.5),
                        ori=handRightOri),
                    Xfo(sc=Vec3(y=1.0, x=1.0, z=1.0),
                        tr=Vec3(x=-8.564000129699707, y=12.281900405883789, z=0.5),
                        ori=handRightOri)
                ]
            }
        })

        legLeftComponentGuide = LegComponentGuide('leg', parent=self)
        legRightComponentGuide = LegComponentGuide('leg', parent=self)
        legRightComponentGuide.loadData({
            "name": 'leg',
            "location": 'R',
            "createIKHandle": False,
            "femurXfo": Xfo(Vec3(-1.0, 9.75, -0.5)),
            "kneeXfo": Xfo(Vec3(-1.5, 5.5, -0.5)),
            "ankleXfo": Xfo(Vec3(-1.75, 1.15, -1.25))
        })

        footLeftComponentGuide = FootComponentGuide('foot', parent=self)
        footRightComponentGuide = FootComponentGuide('foot', parent=self)
        footRightComponentGuide.loadData({
            "name": 'foot',
            "location": 'R',
            'ankleXfo': Xfo(Vec3(-1.75, 1.15, -1.25)),
            'toeXfo': Xfo(Vec3(-1.75, 0.4, 0.25)),
            'toeTipXfo': Xfo(Vec3(-1.75, 0.4, 1.5)),
            'backPivotXfo': Xfo(Vec3(-1.75, 0.0, -2.5)),
            'frontPivotXfo': Xfo(Vec3(-1.75, 0.0, 2.0)),
            'outerPivotXfo': Xfo(Vec3(-2.5, 0.0, -1.25)),
            'innerPivotXfo': Xfo(Vec3(-1.0, 0.0, -1.25))
        })

        # ============
        # Connections
        # ============

        # =======
        # Outputs
        # =======
        mainSrtRigScaleOutput = mainSrtComponentGuide.getOutputByName('rigScale')
        mainSrtOffsetOutput = mainSrtComponentGuide.getOutputByName('offset')
        spineEndOutput = spineComponentGuide.getOutputByName('spineEnd')
        neckEndOutput = neckComponentGuide.getOutputByName('neckEnd')
        clavicleLeftEndOutput = clavicleLeftComponentGuide.getOutputByName('clavicleEnd')
        clavicleRightEndOutput = clavicleRightComponentGuide.getOutputByName('clavicleEnd')
        spinePelvisOutput = spineComponentGuide.getOutputByName('pelvis')

        # Arm Left
        armLeftWristOutput = armLeftComponentGuide.getOutputByName('wrist')

        # Arm Right
        armRightWristOutput = armRightComponentGuide.getOutputByName('wrist')

        # Leg Left
        legLeftIkHandleOutput = legLeftComponentGuide.getOutputByName('ikHandle')
        legLeftLegEndOutput = legLeftComponentGuide.getOutputByName('legEnd')
        legLeftLegEndFKOutput = legLeftComponentGuide.getOutputByName('legEndFK')

        # Leg Right
        legRightIkHandleOutput = legRightComponentGuide.getOutputByName('ikHandle')
        legRightLegEndOutput = legRightComponentGuide.getOutputByName('legEnd')
        legRightLegEndFKOutput = legRightComponentGuide.getOutputByName('legEndFK')

        # Foot Left
        footLeftIkTargetOutput = footLeftComponentGuide.getOutputByName('ikTarget')

        # Foot Right
        footRightIkTargetOutput = footRightComponentGuide.getOutputByName('ikTarget')

        # =========================
        # Inputs & Set Connections
        # =========================
        # Spine
        spineGlobalSrtInput = spineComponentGuide.getInputByName('globalSRT')
        spineGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        spineRigScaleInput = spineComponentGuide.getInputByName('rigScale')
        spineRigScaleInput.setConnection(mainSrtRigScaleOutput)

        # Neck
        neckGlobalSrtInput = neckComponentGuide.getInputByName('globalSRT')
        neckGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        neckSpineEndInput = neckComponentGuide.getInputByName('neckBase')
        neckSpineEndInput.setConnection(spineEndOutput)

        # Head
        headGlobalSrtInput = headComponentGuide.getInputByName('globalSRT')
        headGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        headBaseInput = headComponentGuide.getInputByName('neckRef')
        headBaseInput.setConnection(neckEndOutput)

        headBaseInput = headComponentGuide.getInputByName('worldRef')
        headBaseInput.setConnection(mainSrtOffsetOutput)

        # Clavicle Left
        clavicleLeftGlobalSrtInput = clavicleLeftComponentGuide.getInputByName('globalSRT')
        clavicleLeftGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        clavicleLeftSpineEndInput = clavicleLeftComponentGuide.getInputByName('spineEnd')
        clavicleLeftSpineEndInput.setConnection(spineEndOutput)

        # Clavicle Right
        clavicleRightGlobalSrtInput = clavicleRightComponentGuide.getInputByName('globalSRT')
        clavicleRightGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        clavicleRightSpineEndInput = clavicleRightComponentGuide.getInputByName('spineEnd')
        clavicleRightSpineEndInput.setConnection(spineEndOutput)

        # Arm Left
        armLeftGlobalSrtInput = armLeftComponentGuide.getInputByName('globalSRT')
        armLeftGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        armLeftRigScaleInput = armLeftComponentGuide.getInputByName('rigScale')
        armLeftRigScaleInput.setConnection(mainSrtRigScaleOutput)

        armLeftClavicleEndInput = armLeftComponentGuide.getInputByName('root')
        armLeftClavicleEndInput.setConnection(clavicleLeftEndOutput)

        # Arm Right
        armRightGlobalSrtInput = armRightComponentGuide.getInputByName('globalSRT')
        armRightGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        armRightRigScaleInput = armRightComponentGuide.getInputByName('rigScale')
        armRightRigScaleInput.setConnection(mainSrtRigScaleOutput)

        armRightClavicleEndInput = armRightComponentGuide.getInputByName('root')
        armRightClavicleEndInput.setConnection(clavicleRightEndOutput)

        # Hand Left
        handLeftGlobalSrtInput = handLeftComponentGuide.getInputByName('globalSRT')
        handLeftGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        handLeftArmEndInput = handLeftComponentGuide.getInputByName('armEnd')
        handLeftArmEndInput.setConnection(armLeftWristOutput)

        # Hand Right
        handRightGlobalSrtInput = handRightComponentGuide.getInputByName('globalSRT')
        handRightGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        handRightArmEndInput = handRightComponentGuide.getInputByName('armEnd')
        handRightArmEndInput.setConnection(armRightWristOutput)

        # Leg Left
        legLeftGlobalSrtInput = legLeftComponentGuide.getInputByName('globalSRT')
        legLeftGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        legLeftRigScaleInput = legLeftComponentGuide.getInputByName('rigScale')
        legLeftRigScaleInput.setConnection(mainSrtRigScaleOutput)

        legLeftPelvisInput = legLeftComponentGuide.getInputByName('pelvisInput')
        legLeftPelvisInput.setConnection(spinePelvisOutput)

        legLeftPelvisInput = legLeftComponentGuide.getInputByName('ikTarget')
        legLeftPelvisInput.setConnection(footLeftIkTargetOutput)

        # Leg Right
        legRightGlobalSrtInput = legRightComponentGuide.getInputByName('globalSRT')
        legRightGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        legRightRigScaleInput = legRightComponentGuide.getInputByName('rigScale')
        legRightRigScaleInput.setConnection(mainSrtRigScaleOutput)

        legRightPelvisInput = legRightComponentGuide.getInputByName('pelvisInput')
        legRightPelvisInput.setConnection(spinePelvisOutput)

        legRightPelvisInput = legRightComponentGuide.getInputByName('ikTarget')
        legRightPelvisInput.setConnection(footRightIkTargetOutput)

        # Foot Left
        footLeftGlobalSrtInput = footLeftComponentGuide.getInputByName('globalSRT')
        footLeftGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        footLeftIkHandleInput = footLeftComponentGuide.getInputByName('ikHandle')
        footLeftIkHandleInput.setConnection(legLeftIkHandleOutput)

        footLeftLegEndInput = footLeftComponentGuide.getInputByName('legEnd')
        footLeftLegEndInput.setConnection(legLeftLegEndOutput)

        footLeftLegEndFKInput = footLeftComponentGuide.getInputByName('legEndFK')
        footLeftLegEndFKInput.setConnection(legLeftLegEndFKOutput)


        # Foot Right
        footRightGlobalSrtInput = footRightComponentGuide.getInputByName('globalSRT')
        footRightGlobalSrtInput.setConnection(mainSrtOffsetOutput)

        footRightIkHandleInput = footRightComponentGuide.getInputByName('ikHandle')
        footRightIkHandleInput.setConnection(legRightIkHandleOutput)

        footRightLegEndInput = footRightComponentGuide.getInputByName('legEnd')
        footRightLegEndInput.setConnection(legRightLegEndOutput)

        footRightLegEndFKInput = footRightComponentGuide.getInputByName('legEndFK')
        footRightLegEndFKInput.setConnection(legRightLegEndFKOutput)

        Profiler.getInstance().pop()


if __name__ == "__main__":
    from kraken import plugins

    try:
        Profiler.getInstance().push('bob_guide_build')

        bipedGuide = BobGuideRig('char_bob_guide')

        builder = plugins.getBuilder()
        builder.build(bipedGuide)

    finally:
        Profiler.getInstance().pop()

    print Profiler.getInstance().generateReport()

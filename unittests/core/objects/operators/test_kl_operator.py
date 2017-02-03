
import unittest

from kraken.core.maths import *
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.components.component_output import ComponentOutput
from kraken.core.objects.components.component_output_port import ComponentOutputPort
from kraken.core.objects.operators.kl_operator import KLOperator


class TestKLOperator(unittest.TestCase):

    def testGetSolverTypeName(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')

        self.assertEqual(testOp.getSolverTypeName(), 'TwoBoneIKSolver')

    def testGetExtension(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')

        self.assertEqual(testOp.getExtension(), 'Kraken')

    def testGetSolverArgs(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')
        solverArgs = testOp.getSolverArgs()

        self.assertEqual(len(solverArgs), 15)

    def testGetInputType(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')
        drawDebugType = testOp.getInputType('drawDebug')

        self.assertEqual(drawDebugType, 'Boolean')

    def testGetOutputType(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')
        drawDebugType = testOp.getOutputType('bone0Out')

        self.assertEqual(drawDebugType, 'Mat44')

    def testGetDefaultValue(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')

        self.assertEqual(testOp.getDefaultValue('ikblend', 'Scalar').getSimpleType(), 0.0)

    def testGetInput(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')
        ikBlendInput = testOp.getInput('ikblend')

        self.assertIsNotNone(ikBlendInput)
        self.assertEqual(ikBlendInput, 0.0)
        self.assertTrue(type(ikBlendInput) is float)

    def testGenerateSourceCode(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')

        self.assertTrue(type(testOp.generateSourceCode()) is str)

    def testEvaluate(self):
        testOp = KLOperator('ikSolver', 'TwoBoneIKSolver', 'Kraken')

        femurXfo = Xfo()
        femurXfo.ori = Quat(Vec3(0.739961385727, -0.67020791769, -0.0422816127539), 0.0386102125049)
        femurXfo.tr = Vec3(0.981100022793, 9.76900005341, -0.457199990749)
        femurXfo.sc = Vec3(1.0, 1.0, 1.0)

        kneeXfo = Xfo()
        kneeXfo.ori = Quat(Vec3(0.734117984772, -0.671135187149, -0.1019872576), -0.0157190468162)
        kneeXfo.tr = Vec3(1.40799999237, 5.43709993362, -0.504299998283)
        kneeXfo.sc = Vec3(1.0, 1.0, 1.0)

        handleXfo = Xfo()
        handleXfo.ori = Quat(Vec3(0.0, 0.0, 0.0), 1.0)
        handleXfo.tr = Vec3(1.75, 1.14999997616, -1.25)
        handleXfo.sc = Vec3(1.0, 1.0, 1.0)

        upVXfo = Xfo()
        upVXfo.ori = Quat(Vec3(-0.0114182513207, 0.0722338929772, -0.671222090721), 0.737640023232)
        upVXfo.tr = Vec3(2.01746797562, 5.03647565842, 4.44221878052)
        upVXfo.sc = Vec3(1.0, 1.0, 1.0)


        testOp.setInput('drawDebug', BoolAttribute('drawDebug', False))
        testOp.setInput('rigScale', ScalarAttribute('rigScale', 1.0))
        testOp.setInput('rightSide', BoolAttribute('drawDebug', False))
        testOp.setInput('ikblend', ScalarAttribute('ikblend', 1.0))
        testOp.setInput('root', femurXfo.toMat44())
        testOp.setInput('bone0FK', femurXfo.toMat44())
        testOp.setInput('bone1FK', kneeXfo.toMat44())
        testOp.setInput('ikHandle', handleXfo.toMat44())
        testOp.setInput('upV', upVXfo.toMat44())
        testOp.setInput('bone0Len', 4.35313892365)
        testOp.setInput('bone1Len', 4.3648891449)

        # Need to create outputports and outputs to be able to pull values
        # after eval
        bone0OutputPort = ComponentOutputPort('bone0OutputPort', None, 'Mat44')
        bone0Output = ComponentOutput('bone0Output')
        bone0OutputPort.setTarget(bone0Output)

        bone1OutputPort = ComponentOutputPort('bone1OutputPort', None, 'Mat44')
        bone1Output = ComponentOutput('bone1Output')
        bone1OutputPort.setTarget(bone1Output)

        bone2OutputPort = ComponentOutputPort('bone2OutputPort', None, 'Mat44')
        bone2Output = ComponentOutput('bone2Output')
        bone2OutputPort.setTarget(bone2Output)

        midJointOutputPort = ComponentOutputPort('midJointOutputPort', None, 'Mat44')
        midJointOutput = ComponentOutput('midJointOutput')
        midJointOutputPort.setTarget(midJointOutput)

        testOp.setOutput('bone0Out', bone0OutputPort.getTarget())
        testOp.setOutput('bone1Out', bone1OutputPort.getTarget())
        testOp.setOutput('bone2Out', bone2OutputPort.getTarget())
        testOp.setOutput('midJointOut', midJointOutputPort.getTarget())

        # Check pre eval
        self.assertEqual(str(testOp.outputs['bone0Out'].xfo.tr), "Vec3(0.0, 0.0, 0.0)")
        self.assertEqual(str(testOp.outputs['bone1Out'].xfo.tr), "Vec3(0.0, 0.0, 0.0)")
        self.assertEqual(str(testOp.outputs['bone2Out'].xfo.tr), "Vec3(0.0, 0.0, 0.0)")
        self.assertEqual(str(testOp.outputs['midJointOut'].xfo.tr), "Vec3(0.0, 0.0, 0.0)")

        testOp.evaluate()

        # Check post eval
        self.assertEqual(str(testOp.outputs['bone0Out'].xfo.tr), "Vec3(0.981100022793, 9.76900005341, -0.457199990749)")
        self.assertEqual(str(testOp.outputs['bone1Out'].xfo.tr), "Vec3(1.40800035, 5.4371008873, -0.504299998283)")
        self.assertEqual(str(testOp.outputs['bone2Out'].xfo.tr), "Vec3(1.75000023842, 1.15000009537, -1.25000023842)")
        self.assertEqual(str(testOp.outputs['midJointOut'].xfo.tr), "Vec3(1.40800035, 5.4371008873, -0.504299998283)")


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestKLOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)


import unittest

from kraken.core.maths import *
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.operators.canvas_operator import CanvasOperator


class TestCanvasOperator(unittest.TestCase):

    def testGetDefaultValue(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertEqual(testOp.getDefaultValue('drawDebug', 'Boolean'), False)

    def testGetPresetPath(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertEqual(testOp.getPresetPath(), 'Kraken.Solvers.Biped.BipedFootSolver')

    def testGetGraphDesc(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertRaises(DeprecationWarning, lambda: testOp.getGraphDesc())

    def testGetInput(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertEqual(testOp.getInput('drawDebug'), False)

    def testGetInputType(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertEqual(testOp.getInputType('drawDebug'), 'Boolean')

    def testGetOutputType(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        self.assertEqual(testOp.getOutputType('ankle_result'), 'Mat44')

    def testEvaluate(self):
        testOp = CanvasOperator('footSolver', 'Kraken.Solvers.Biped.BipedFootSolver')

        ikBlend = ScalarAttribute('ikBlend', 1.0)
        ankleLen = ScalarAttribute('ankleLen', 1.67705094814)
        toeLen = ScalarAttribute('toeLen', 1.25)

        legEnd = Xfo()
        legEnd.ori = Quat(Vec3(0.0, 0.0, 0.0), 1.0)
        legEnd.tr = Vec3(1.75, 1.14999997616, -1.25)
        legEnd.sc = Vec3(1.0, 1.0, 1.0)
        legEnd = legEnd.toMat44()

        ankleIK = Xfo()
        ankleIK.ori = Quat(Vec3(0.162459865212, -0.688190937042, -0.162459850311), 0.688191056252)
        ankleIK.tr = Vec3(1.75, 0.40000000596, 0.25)
        ankleIK.sc = Vec3(1.0, 1.0, 1.0)
        ankleIK = ankleIK.toMat44()

        toeIK = Xfo()
        toeIK.ori = Quat(Vec3(-0.0, -0.70710682869, 0.0), 0.70710682869)
        toeIK.tr = Vec3(1.75, 0.40000000596, 0.25)
        toeIK.sc = Vec3(1.0, 1.0, 1.0)
        toeIK = toeIK.toMat44()

        ankleFK = Xfo()
        ankleFK.ori = Quat(Vec3(0.601501047611, -0.601500928402, 0.371748030186), 0.37174808979)
        ankleFK.tr = Vec3(1.75, 0.40000000596, 0.25)
        ankleFK.sc = Vec3(1.0, 1.0, 1.0)
        ankleFK = ankleFK.toMat44()

        toeFK = Xfo()
        toeFK.ori = Quat(Vec3(0.5, -0.5, 0.5), 0.5)
        toeFK.tr = Vec3(1.75, 0.40000000596, 0.25)
        toeFK.sc = Vec3(1.0, 1.0, 1.0)
        toeFK = toeFK.toMat44()

        testOp.setInput('drawDebug', BoolAttribute('drawDebug', False))
        testOp.setInput('rigScale', ScalarAttribute('rigScale', 1.0))
        testOp.setInput('ikBlend', ikBlend)
        testOp.setInput('ankleLen', ankleLen)
        testOp.setInput('toeLen', toeLen)
        testOp.setInput('legEnd', legEnd)
        testOp.setInput('ankleIK', ankleIK)
        testOp.setInput('toeIK', toeIK)
        testOp.setInput('ankleFK', ankleFK)
        testOp.setInput('toeFK', toeFK)
        testOp.evaluate()

        ankleResult = testOp.binding.getArgValue('ankle_result')
        self.assertEqual(round(ankleResult.row0.t.getSimpleType(), 2), 1.75)
        self.assertEqual(round(ankleResult.row1.t.getSimpleType(), 2), 1.15)
        self.assertEqual(round(ankleResult.row2.t.getSimpleType(), 2), -1.25)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCanvasOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)

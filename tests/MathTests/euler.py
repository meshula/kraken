import json

from kraken.core.maths import *


euler = Euler()
print "euler:" + str(euler)
print "mat33:" + str(euler.toMat33())
euler = Euler(1.0, 0.0, 2.0, 'ZYX')
print "euler:" + str(euler)
print "mat33:" + str(euler.toMat33())
print "clone:" + str(euler.clone())

euler = Euler(1.0, 0.0, 2.0, RotationOrder())
print "euler:" + str(euler)

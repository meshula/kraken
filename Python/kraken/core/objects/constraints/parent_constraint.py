"""Kraken - objects.Constraints.ParentConstraint module.

Classes:
ParentConstraint - Parent Constraint.

"""

from constraint import Constraint
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.quat import Quat


class ParentConstraint(Constraint):
    """Pose Constraint."""

    def __init__(self, name, metaData=None):
        super(ParentConstraint, self).__init__(name, metaData=metaData)


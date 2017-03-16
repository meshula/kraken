"""Kraken - objects.Constraints.PositionConstraint module.

Classes:
PositionConstraint - Position Constraint.

"""

from constraint import Constraint
from kraken.core.maths.vec3 import Vec3


class GlueConstraint(Constraint):
    """Special type of constraint that does not factor into dependency graph,

    Creating and setting inputs and outputs of this constraint does not set "source"
    or "depends" linkage so these nodes are not found by the traverser.  They would most
    likely cause cycles.

    They are primarily used in a KL Rig when needing to "glue" control objects to the inPoseJointMatrices
    """

    def __init__(self, name, metaData=None):
        super(GlueConstraint, self).__init__(name, metaData=metaData)

        self._space_constrainee = None  # Must be Object3D
        self._space_constrainers = []  # Must be Joint

    def setConstrainee(self, constrainee):
        """Sets the constrainee object for this constraint.

        Args:
            constrainee (Object): Object that will be constrained.

        Returns:
            bool: True if successful.

        """

        if kObject3D.isTypeOf("Joint"):
            raise Exception("'constrainee' argument cannot be a Joint."
                +"  Joints drive Object3Ds with GlueConstraints.")

        self._constrainee = constrainee
        # Do not add to self source like other constraints

        return True

    def setConstrainer(self, kObject3D, index=0):
        """Sets the constrainer at the specified index.

        Args:
            kObject3D (object): Kraken 3D object.
            index (int): index of the constraint to set.

        Returns:
            bool: True if successful.

        """

        if not kObject3D.isTypeOf("Joint"):
            raise Exception("'kObject3D' argument is not a Joint.  "
                +" Only joints can be used as constrainers for GlueConstraints.")

        super(GlueConstraint, self).setConstrainer(kObject3D, index=index)

        return True

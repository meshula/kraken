"""Kraken - maths.rotation_order module.

Classes:
RotationOrder -- Rotation Order.
"""

import math

from kraken.core.maths.constants import ROT_ORDER_INT_TO_STR_MAP
from kraken.core.maths.constants import ROT_ORDER_STR_TO_INT_MAP
from kraken.core.kraken_system import ks
from kraken.core.maths.math_object import MathObject


class RotationOrder(MathObject):
    """RotationOrder rotation object."""

    def __init__(self, order=4):
        """Initialize rotation order."""

        super(RotationOrder, self).__init__()

        if ks.getRTValTypeName(order) == 'RotationOrder':
            self._rtval = order
        else:
            self._rtval = ks.rtVal('RotationOrder')
            if isinstance(order, RotationOrder):
                self.set(order=order.order)
            else:
                self.set(order=order)


    def __str__(self):
        """String representation of RotationOrder object.

        Returns:
            str: String representation of the RotationOrder.

        """

        return "RotationOrder(order='" + str(self.order) + "')"


    @property
    def order(self):
        """Gets order value of this Rotation Order.

        Returns:
            float: Order value of this Rotation Order.

        """

        return self._rtval.order.getSimpleType()


    @order.setter
    def order(self, value):
        """Sets order value from the input value.

        Args:
            value (int, str): Value to set the order property as.

        Returns:
            bool: True if successful.

        """

        self._rtval.order = ks.rtVal('Integer', value)

        return True


    def __eq__(self, other):
        return self.order == other.order

    def __ne__(self, other):
        return not self.order == other.order


    def clone(self):
        """Returns a clone of the RotationOrder.

        Returns:
            RotationOrder: The cloned RotationOrder.

        """

        rotOrder = RotationOrder()
        rotOrder.order = self.order

        return rotOrder


    def set(self, order):
        """Sets the order value from the input values.

        Args:
            order (int, str): Value to set the order property as.

        Returns:
            bool: True if successful.

        """

        if type(order) == str:
            newOrder = ROT_ORDER_STR_TO_INT_MAP.get(order, -1)
            if newOrder == -1:
                print "Invalid rotation order string: '" + order + "', using default 4 (XYZ)."
                newOrder = 4

        elif type(order) == int:
            if order not in ROT_ORDER_INT_TO_STR_MAP:
                print "Invalid rotation order index: '" + str(order) + "', using default 4 (XYZ)."
                newOrder = 4
            else:
                newOrder = order
        else:
            raise NotImplementedError("Cannot set rotation order with type: " + str(type(order)))

        if newOrder == 0:
            self._rtval.setZYX('')
        elif newOrder == 1:
            self._rtval.setXZY('')
        elif newOrder == 2:
            self._rtval.setYXZ('')
        elif newOrder == 3:
            self._rtval.setYZX('')
        elif newOrder == 4:
            self._rtval.setXYZ('')
        elif newOrder == 5:
            self._rtval.setZXY('')
        else:
            raise ValueError("Invalid rotation order: '" + str(order) + "'")

        return True


    def isZYX(self):
        """Checks if this Rotation Order is equal to ZYX.

        Returns:
            bool: True if this rotationorder is ZYX.

        """

        return self.order == 0


    def isXZY(self):
        """Checks if this Rotation Order is equal to XZY.

        Returns:
            bool: True if this rotationorder is XZY.

        """

        return self.order == 1


    def isYXZ(self):
        """Checks if this Rotation Order is equal to YXZ.

        Returns:
            bool: True if this rotationorder is YXZ.

        """

        return self.order == 2


    def isYZX(self):
        """Checks if this Rotation Order is equal to YZX.

        Returns:
            bool: True if this rotationorder is YZX.

        """

        return self.order == 3


    def isXYZ(self):
        """Checks if this Rotation Order is equal to XYZ.

        Returns:
            bool: True if this rotationorder is XYZ.

        """

        return self.order == 4


    def isZXY(self):
        """Checks if this Rotation Order is equal to ZXY.

        Returns:
            bool: True if this rotationorder is ZXY.

        """

        return self.order == 5


    def isReversed(self):
        """Checks if this Rotation Order is a reversed one.

        Returns:
            bool: True if this rotation order is one of the reversed ones (XZY, ZYX or YXZ).

        """

        return self.isXZY() or self.isZYX() or self.isYXZ()


    def setZYX(self):
        """Sets this rotation order to be ZYX.

        Returns:
            bool: True if successful.

        """

        self._rtval.setZYX('')

        return True


    def setXZY(self):
        """Sets this rotation order to be XZY.

        Returns:
            bool: True if successful.

        """

        self._rtval.setXZY('')

        return True


    def setYXZ(self):
        """Sets this rotation order to be YXZ.

        Returns:
            bool: True if successful.

        """

        self._rtval.setYXZ('')

        return True


    def setYZX(self):
        """Sets this rotation order to be YZX.

        Returns:
            bool: True if successful.

        """

        self._rtval.setYZX('')

        return True


    def setXYZ(self):
        """Sets this rotation order to be XYZ.

        Returns:
            bool: True if successful.

        """

        self._rtval.setXYZ('')

        return True


    def setZXY(self):
        """Sets this rotation order to be ZXY.

        Returns:
            bool: True if successful.

        """

        self._rtval.setZXY('')

        return True

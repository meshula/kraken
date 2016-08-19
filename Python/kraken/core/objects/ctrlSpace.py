"""Kraken - objects.ctrlSpace module.

Classes:
CtrlSpace -- CtrlSpace representation.

"""

from kraken.core.objects.object_3d import Object3D


class CtrlSpace(Object3D):
    """CtrlSpace object."""

    def __init__(self, name, parent=None, flags=None):
        super(CtrlSpace, self).__init__(name, parent=parent, flags=flags)
        self.setShapeVisibility(False)


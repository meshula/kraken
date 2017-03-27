"""Kraken - objects.ctrlSpace module.

Classes:
CtrlSpace -- CtrlSpace representation.

"""

import kraken.core.objects.object_3d


class Space(kraken.core.objects.object_3d.Object3D):
    """Space object.
    By default, it shares the same xfo as it's child.
    Thus, Parent and child are always co-located until build time
    No need to always set the xfo of this space object
    """


    def __init__(self, name, parent=None, flags=None, metaData=None):
        super(Space, self).__init__(name, parent=parent, flags=flags, metaData=metaData)
        self.setShapeVisibility(False)


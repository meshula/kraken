"""Kraken - traverser module.

Classes:
Traverser - Base Traverser.

"""

from kraken.core.objects.scene_item import SceneItem
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.components.component import Component
from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.constraints.constraint import Constraint
from kraken.core.objects.operators.operator import Operator


class Optimizer(object):
    """Kraken base traverser for any scene item.

    The optimizer iterates through all scene items and collapses resundancies by deleting items and rewiring connections.

    """

    def __init__(self, name='Optimizer'):
        pass

    def optimize(self):
        pass

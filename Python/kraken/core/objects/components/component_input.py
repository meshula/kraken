"""Kraken - objects.components.component_input module.

Classes:
ComponentInput -- ComponentInput representation.

"""

from kraken.core.objects.object_3d import Object3D


class ComponentInput(Object3D):
    """ComponentInput object."""

    def __init__(self, name, parent=None, metaData=None):
        super(ComponentInput, self).__init__(name, parent=parent, metaData=metaData)
        self.setShapeVisibility(False)
        self._scaleCompensate = False  # When constraining inputs

    def setScaleCompensate(self, scaleCompensate):
        """Sets whether scale is ingored when connecting xfos

        Args:
            scaleCompensate (bool): Ignore scale if incoming port xfo

        Returns:
            bool: True if successful.

        """

        self._scaleCompensate = scaleCompensate

        return True

    def getScaleCompensate(self):
        """Returns if ignore scale if incoming port xfo

        Returns:
            bool: True if ignore scale if incoming port xfo

        """

        return self._scaleCompensate
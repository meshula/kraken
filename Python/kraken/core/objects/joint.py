"""Kraken - objects.joint module.

Classes:
Joint -- Joint representation.

"""

from kraken.core.configs.config import Config
from kraken.core.objects.object_3d import Object3D


class Joint(Object3D):
    """Joint object."""

    def __init__(self, name, parent=None, flags=None, metaData=None, **kwargs):
        super(Joint, self).__init__(name, parent=parent, flags=flags, metaData=metaData)
        self._radius = 1.0

        if 'radius' in kwargs:
            jointRadius = kwargs['radius']
        else:
            config = Config.getInstance()
            objSettings = config.getObjectSettings()
            jointSettings = objSettings.get('joint', None)
            if jointSettings is None:
                jointRadius = 1.0
            else:
                jointRadius = jointSettings.get('size', 1.0)

        self.setRadius(jointRadius)


    def getRadius(self):
        """Gets the radius of the joint.

        Returns:
            float: Radius of the joint.

        """

        return self._radius

    def setRadius(self, radius):
        """Sets the radius of the joint.

        Args:
            radiu (float): Radius to set the joint to.

        Returns:
            bool: True if successful.

        """

        assert type(radius) in (int, float), "Joint.setRadius() argument value" \
            "is of type '" + type(radius).__name__ + "' , not of type (int, float)"

        if type(radius) is int:
            radius = float(radius)

        self._radius = radius

        return True

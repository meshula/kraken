from kraken.core.objects.control import Control

class FKControl(Control):
    """Mocap control object."""

    def __init__(self, name, parent=None, shape="null", scale=1.0):
        super(self.__class__, self).__init__(name, parent=parent, shape=shape, scale=scale)


class IKControl(Control):
    """Mocap control object."""

    def __init__(self, name, parent=None, shape="null", scale=1.0):
        super(self.__class__, self).__init__(name, parent=parent, shape=shape, scale=scale)

class MCControl(Control):
    """Mocap control object."""

    def __init__(self, name, parent=None, shape="null", scale=1.0):
        super(self.__class__, self).__init__(name, parent=parent, shape=shape, scale=scale)

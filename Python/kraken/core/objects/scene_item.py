"""Kraken - objects.scene_item module.

Classes:
SceneItem - Base SceneItem Object.

"""
import inspect

class SceneItem(object):
    """Kraken base object type for any 3D object."""

    def __init__(self, name, parent=None):
        super(SceneItem, self).__init__()
        self._parent = parent
        self._name = name
        self._secondBuildNameType = None



    # ==============
    # Type Methods
    # ==============
    def getTypeName(self):
        """Returns the class name of this object.

        Returns:
            bool: True if successful.

        """

        return self.__class__.__name__


    def getTypeHierarchyNames(self):
        """Returns the class name of this object.

        Returns:
            bool: True if successful.

        """

        khierarchy = []
        for cls in type.mro(type(self)):
            if cls == object:
                break
            khierarchy.append(cls.__name__)

        return khierarchy


    def isTypeOf(self, typeName):
        """Returns the class name of this object.

        Returns:
            bool: True if the scene item is of the given type.

        """

        for cls in type.mro(type(self)):
            if cls.__name__ == typeName:
                return True

        return False


    # =============
    # Name methods
    # =============
    def getName(self):
        """Returns the name of the object as a string.

        Returns:
            str: Object's name.

        """

        return self._name


    def setName(self, name):
        """Sets the name of the object with a string.

        Arguments:
            name (str): The new name for the item.

        Returns:
            bool: True if successful.

        """

        self._name = name

        return True


    def getPath(self):
        """Returns the full hierarchical path to this object.

        Returns:
            str: Full name of the object.

        """

        if self.getParent() is not None:
            return self.getParent().getPath() + '.' + self.getName()

        return self.getName()


    def getNameDecoration(self):
        """Gets the decorated name of the object.

        Returns:
            str: Decorated name of the object.

        """
        decoration = ":"+self.__class__.__name__

        if self.getSecondType():
            decoration += ":"+self.getSecondType().__name__

        return decoration


    def getDecoratedName(self):
        """Gets the decorated name of the object.

        Returns:
            str: Decorated name of the object.

        """

        return self.getName() + self.getNameDecoration()


    def getDecoratedPath(self):
        """Gets the decorated path of the object.

        Returns:
            str: Decorated path  of the object.

        """


        if self.getParent() is not None:
            return self.getParent().getDecoratedPath() + '.' + self.getDecoratedName()

        return self.getDecoratedName()


    # ===============
    # Parent Methods
    # ===============
    def getParent(self):
        """Returns the parent of the object as an object.

        Returns:
            Object: Parent of this object.

        """

        return self._parent


    def setParent(self, parent):
        """Sets the parent attribute of this object.

        Arguments:
        parent (Object): Object that is the parent of this one.

        Returns:
            bool: True if successful.

        """

        self._parent = parent

        return True

    def getSecondType(self):
        """Returns the second type of the object as a class.

        Returns:
            Class: second type of the object as a class.

        """

        return self._secondBuildNameType


    def setSecondType(self, objectClass):
        """Sets the second type of the object as a class.

        Args:
            type (Class): Class that is the secondary type (for use in getBuildName() later)
            Maybe allow this to be a string later on for flexibilty?

        Returns:
            bool: True if successful.

        """

        self._secondBuildNameType = objectClass

        return True

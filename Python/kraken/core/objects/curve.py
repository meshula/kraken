"""Kraken - objects.curve module.

Classes:
Curve - Curve.

"""

import copy

from kraken.core.objects.object_3d import Object3D


class Curve(Object3D):
    """Curve object."""

    def __init__(self, name, parent=None, flags=None, metaData=None):
        super(Curve, self).__init__(name, parent=parent, flags=flags, metaData=metaData)

        self._data = None


    # ======================
    # Control Point Methods
    # ======================
    def getCurveData(self):
        """Returns the data of the curve.

        Returns:
            list: Dictionaries defining each sub-curve of this curve.

        """

        return self._data


    def setCurveData(self, data):
        """Sets the curve data.

        Arguments:
        data (list): Dictionaries defining each sub-curve of this curve.

        Returns:
            bool: True if successful.

        """

        dataErrorMsg = ("Curve Object '{}', sub-curve[{}] data does not contain "
                        "required '{}' data.")

        for i, subCurve in enumerate(data):
            assert 'points' in subCurve, dataErrorMsg.format(self.getName(), str(i), 'points')
            assert 'degree' in subCurve, dataErrorMsg.format(self.getName(), str(i), 'degree')
            assert 'closed' in subCurve, dataErrorMsg.format(self.getName(), str(i), 'closed')

        self._data = copy.deepcopy(data)

        return True


    def appendCurveData(self, data):
        """Appends sub-curve data to this curve.

        Arguments:
        data (list): Dictionaries defining each sub-curve being added to this
        curve.

        Returns:
            bool: True if successful.

        """

        if self._data is None:
            raise ValueError("Curve object has no curve data to append to.")

        self._data += data

        return True


    # ==================
    # Sub-Curve Methods
    # ==================
    def checkSubCurveIndex(self, index):
        """Checks the supplied index is valid.

        Args:
            index (int): Sub-curve index to check.

        """

        if index > len(self.getCurveData()) - 1:
            errMsg = "Invalid index [{}], out of the range [{}] of the 'data' array."
            raise IndexError(errMsg.format(str(index), str(len(self.getCurveData()) - 1)))

        return True


    def getNumSubCurves(self):
        """Returns the number of sub-curves on this object.

        Returns:
            int: Number of sub-curves in this object.

        """

        return len(self.getCurveData())


    def getSubCurveClosed(self, index):
        """Returns whether the sub-curve is closed or not.

        Args:
            index (int): Index of the sub-curve to query.

        Returns:
            bool: True if the sub-curve is closed.

        """

        if self.checkSubCurveIndex(index) is not True:
            return False

        return self._data[index]["closed"]


    def getSubCurveData(self, index):
        """Get the sub-curve data by it's index.

        Arguments:
            index (int): Index of the sub-curve to get the data for.

        Returns:
            dict: Data defining the sub-curve.

        """

        if self.checkSubCurveIndex(index) is not True:
            return False

        return self._data[index]


    def setSubCurveData(self, index, data):
        """Sets the sub-curve data.

        Arguments:
            index (int): Index of the sub-curve to get the data for.
            data (dict): Defining the sub-curve data.

        Returns:
            bool: True if successful.

        """

        if self.checkSubCurveIndex(index) is not True:
            return False

        self._data[index] = data

        return True


    def removeSubCurveByIndex(self, index):
        """Removes a sub-curve by its index.

        Args:
            index (int): Index of the sub-curve to remove.

        Returns:
            bool: True if successful.

        """

        if self.checkSubCurveIndex(index) is not True:
            return False

        del self._data[index]

        return True

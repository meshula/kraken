import pymel.core as pm
import pymel.util as pmUtil
import pymel.core.datatypes as dt

from maya import OpenMaya as om

from maya import cmds


def lockObjXfo(dccSceneItem, lock=True):
    """Locks the dccSceneItem's transform parameters.

    Args:
        dccSceneItem (Object): DCC object to lock transform parameters on.

    Returns:
        bool: True if successful.

    """

    localXfoParams = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    for eachParam in localXfoParams:
        pm.setAttr(dccSceneItem.longName() + "." + eachParam, lock=lock, keyable=False, channelBox=False)

    return True


class TemporarilyUnlockXfo():
    """When used in "with" statement, temporarily unlocks attributes in given scope of "with"

    Args:
        dccSceneItem (Object): DCC object to unlock transform parameters on.

    """

    def __init__(self, dccSceneItem):
        self.node = dccSceneItem
        self.localXfoDict = {'tx': False, 'ty': False, 'tz': False, 'rx': False, 'ry': False, 'rz': False, 'sx': False, 'sy': False, 'sz': False}
    def __enter__(self):
        for key in self.localXfoDict.keys():
            self.localXfoDict[key] = pm.getAttr(self.node.longName() + "." + key, lock=True)
            pm.setAttr(self.node.longName() + "." + key, lock=False)
        return self
    def __exit__(self, type, value, traceback):
        for key in self.localXfoDict.keys():
            pm.setAttr(self.node.longName() + "." + key, lock=self.localXfoDict[key])

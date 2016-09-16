import pymxs
import MaxPlus

rt = pymxs.runtime


def lockObjXfo(dccSceneItem):
    """Locks the dccSceneItem's transform parameters.

    Args:
        dccSceneItem (Object): DCC object to lock transform parameters on.

    Returns:
        bool: True if successful.

    """

    # localXfoParams = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    # for eachParam in localXfoParams:
    #     pm.setAttr(dccSceneItem.longName() + "." + eachParam, lock=True, keyable=False, channelBox=False)

    return True

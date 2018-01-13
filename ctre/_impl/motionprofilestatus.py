# validated: 2018-01-06 EN d090f9cdc6a1 libraries/driver/include/ctre/phoenix/Motion/MotionProfileStatus.h
from collections import namedtuple


__all__ = ['MotionProfileStatus']


#: Motion Profile Status.
#: This is simply a data transfer object.
MotionProfileStatus = namedtuple("MotionProfileStatus", ["topBufferRem", "topBufferCnt", "btmBufferCnt", "hasUnderrun",
                                                         "isUnderrun", "activePointValid", "isLast", "profileSlotSelect", "outputEnable"])
MotionProfileStatus.topBufferRem.__doc__ = """
     The available empty slots in the trajectory buffer.

     The robot API holds a "top buffer" of trajectory points, so your applicaion
     can dump several points at once.  The API will then stream them into the Talon's
     low-level buffer, allowing the Talon to act on them.
"""
MotionProfileStatus.topBufferCnt.__doc__ = "The number of points in the top trajectory buffer."
MotionProfileStatus.btmBufferCnt.__doc__ = "The number of points in the low level Talon buffer."
MotionProfileStatus.hasUnderrun.__doc__ = """
     Set if isUnderrun ever gets set.
     Only is cleared by clearMotionProfileHasUnderrun() to ensure
     robot logic can react or instrument it.
"""
MotionProfileStatus.isUnderrun.__doc__ = """
     This is set if Talon needs to shift a point from its buffer into
     the active trajectory point however the buffer is empty. This gets cleared
     automatically when is resolved.
"""
MotionProfileStatus.activePointValid.__doc__ = """
     True if the active trajectory point has not empty, false otherwise.
     The members in activePoint are only valid if this signal is set.
"""
#MotionProfileStatus.isLast.__doc__ = ""
#MotionProfileStatus.profileSlotSelect.__doc__ = ""
MotionProfileStatus.outputEnable.__doc__ = """
     The current output mode of the motion profile executer (disabled, enabled, or hold).
     When changing the set() value in MP mode, it's important to check this signal to
     confirm the change takes effect before interacting with the top buffer.
"""

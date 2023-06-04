#!/usr/bin/env python3

import rospy
from std_srvs.srv import *
from your_smach.srv import GoToPosition, GoToPositionResponse

class StateMockUp(object):
    def __init__(self) -> None:
        rospy.init_node('state_mockup', anonymous=True)
        rospy.Service('robot/go_to_position', GoToPosition, self.gotopos_callback)
        rospy.Service('robot/do_sth', Empty, self.dosth_callback)

    def gotopos_callback(self, data):
        rospy.loginfo(f'Going to position name: {data.position_name}')
        res = GoToPositionResponse()
        res.success = True
        return res
    
    def dosth_callback(self, data):
        rospy.loginfo("Doing something")
        return EmptyResponse()
    
if __name__ == "__main__":
    mockup = StateMockUp()
    rospy.spin()

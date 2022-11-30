#!/usr/bin/env python3

import rospy
import smach
import smach_ros
from std_srvs.srv import *
from your_smach.srv import GoToPosition, GoToPositionRequest

class DoSth(smach.State):
    def __init__(self, outcomes=['success', 'fail']):
        super().__init__(outcomes)
        self.dosth_ser = rospy.ServiceProxy('robot/do_sth', Empty)
    
    def execute(self, ud):
        rospy.loginfo("Executing state DoSth")
        self.dosth_ser()
        return 'success'

class GoToPosition(smach.State):
    def __init__(self, outcomes=['success', 'fail']):
        super().__init__(outcomes)
        self.gotopos = rospy.ServiceProxy('robot/go_to_position', GoToPosition)
    
    def execute(self, ud):
        rospy.loginfo("Executing state GoToPosition")
        req = GoToPositionRequest()
        req.position_name = 'home'
        self.gotopos(req)
        return 'success' 

class RobotState(object):
    def __init__(self) -> None:
        rospy.init_node('robot_state', anonymous=True)
        sm = smach.StateMachine(outcomes=['---finish---'])

        with sm:
            smach.StateMachine.add('DoSth1', DoSth(), 
                               transitions={'success':'Gotoposition', 'fail':'DoSth1'})
            smach.StateMachine.add('Gotoposition', GoToPosition(), 
                                transitions={'success':'DoSth2', 'fail':'Gotoposition'})
            smach.StateMachine.add('DoSth2', DoSth(), 
                               transitions={'success':'---finish---', 'fail':'DoSth2'})
        outcome = sm.execute()

if __name__ == "__main__":
    RobotState()
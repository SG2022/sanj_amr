#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msgs import Twist 

def callback(data):
    lin = data.linear
    ang = data.angular
    # just considering the sign

    if(lin):
        #move forward
    else: 
        #move backward

    if(ang):
        #move clockwise
    else: 
        #move anti clockwise  


def forward():
    # how to move forward
def backward ():
    # how to move backward 
def right():
    # how to move right 
def left():
    # how to move left

    print(lin)
    print(ang)

def listener():
    rospy.init_node('cmdvel_subscriber', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

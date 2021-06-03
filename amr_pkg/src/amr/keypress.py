#!/usr/bin/env python
import getch
import rospy
from std_msgs.msg import String #String message 
from std_msgs.msg import Int8





def keys():
    rospy.init_node('keypress',anonymous=True)
    pub = rospy.Publisher('key',String,queue_size=10) # "key" is the publisher name
    rate = rospy.Rate(10)#try removing this line ans see what happens

    while not rospy.is_shutdown():
        k=getch.getch()# this is used to convert the keypress event in the keyboard or joypad , joystick to a ord value
       # if ((k>=65)&(k<=68)|(k==115)|(k==113)|(k==97)):# to filter only the up , dowm ,left , right key /// this line can be removed or more key can be added to this
        rospy.loginfo(k)# to print on  terminal 
        pub.publish(k)#to publish
        #rospy.loginfo(str(k))

        #rate.sleep()

#s=115,e=101,g=103,b=98

if __name__=='__main__':
    try:
        keys()
    except rospy.ROSInterruptException:
        pass


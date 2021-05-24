#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msgs import Twist 
import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3 = 22
in4 = 27

en1 = 25
en2 =4
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)


def callback(data):
    p1.start(25)
    p2.start(25)
    lin = data.linear
    ang = data.angular
    # just considering the sign

    if(lin):
        forward()
    else: 
        backward()

    #if(ang):
        #move clockwise
    #else: 
        #move anti clockwise  


def forward():
   
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        print("forward")
    
    
    
    
    
def backward ():
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
#def right():
    # how to move right 
#def left():
    # how to move left

    print(lin)
    print(ang)

def listener():
    rospy.init_node('cmdvel_subscriber', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

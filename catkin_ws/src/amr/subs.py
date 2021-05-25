#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 
import RPi.GPIO as GPIO          
from time import sleep

# defined pins
in1 = 24
in2 = 23
in3 = 22
in4 = 27
en1 = 25
en2 =4
temp1=1

# setup
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

# setting up pwm 
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)
p1.start(25)
p2.start(25)

print("All the pin setup done")

def callback(data):
    x = data.linear.x
    z = data.angular.z
    if (x>0):
       forward()
    elif (x<0): 
       backward()
    elif(z<0):
       right()
    elif(z>0):
       left()
    elif (x==0 and z==0):
       stop()

def forward():
    print("forward")
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)
    GPIO.output(in1,GPIO.HIGH) # anti
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH) # clock
    GPIO.output(in4,GPIO.LOW)

def backward():
    print("backward")
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def right():
    print("right turn")
    p1.ChangeDutyCycle(15)
    p2.ChangeDutyCycle(15)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def left():
    print("left  turn")
    p1.ChangeDutyCycle(15)
    p2.ChangeDutyCycle(15)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():
    print("stop")  
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def listener():
    rospy.init_node('cmdvel_subscriber', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

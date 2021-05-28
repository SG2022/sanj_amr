#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 
import RPi.GPIO as GPIO          
from time import sleep
in1 = 24
in2 = 23
in3 = 22
in4 = 27
en1 = 25
en2 =4
temp1=1

#setting up gpio pins
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

#setting up pwm pins
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)

# initial setup for duty
duty=0
lin=0
ang=0
p1.start(25)
p2.start(25)

def callback(data):
    lin = data.linear.x
    ang = data.angular.z

    # converting into duty cycle from the teleop message by mulitplying it to 10
    duty =( lin * 10)

    # filter if duty cycle exceeds the limit
    if duty > 80:
        duty = 80
    
    if lin>0:
       forward(duty)
    elif lin<0: 
       backward(duty)
    if(ang<0):
       right(duty)
    else: 
       left(duty)  
    if (lin==0 and ang==0):
       stop()

def forward(duty):
    print("forward with duty :{} ".format(duty))
    p1.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def backward(duty):
    print("backward with duty :{} ".format(duty))
    p1.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def right(duty):
    print("right with duty :{} ".format(duty))
    p1.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
 
def left(duty):
    print("left with duty :{} ".format(duty))
    p1.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("stop with duty :{} ".format(duty))

def listener():
    rospy.init_node('cmdvel_subscriber', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

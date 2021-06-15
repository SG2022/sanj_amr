#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist,PoseStamped
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

move_pwm = 60
turn_pwm = 45

p1.start(move_pwm)
p2.start(move_pwm)
max_pwm = 90

curr_pose = PoseStamped()

print("All the pin setup done")

#individual motor pwm
left_motor_pwm = 0
right_motor_pwm = 0

def pose_callback(data):
    global curr_pose
    curr_pose = data.data

def calculate_error():
    pass

def twist_to_motors(data):
    global left_motor_pwm, right_motor_pwm
    # scaling the values for our motor
    dx = data.angular.x * 50
    dr = data.angular.z
    right_motor_pwm = dx + dr * robot_width/2
    left_motor_pwm = dx - dr * robot_width/2
    handle_left_motor(left_motor_pwm)
    handle_right_motor(right_motor_pwm)

def callback(data):
    twist_to_motors(data)

def stop():
    print("stop")  
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def handle_left_motor(pwm):
    p2.ChangeDutyCycle(pwm)
    if(pwm>0):
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    else: 
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

def handle_right_motor(pwm):
    p1.ChangeDutyCycle(pwm)
    if(pwm > 0):
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

def listener():
    rospy.init_node('cmdvel_subscriber', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.Subscriber('slam_out_pose', PoseStamped, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

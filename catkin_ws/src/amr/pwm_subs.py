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

<<<<<<< HEAD
# initial setup for duty
duty=0
lin=0
ang=0
p1.start(25)
p2.start(25)
=======
move_pwm = 60
turn_pwm = 45

p1.start(move_pwm)
p2.start(move_pwm)

max_pwm = 90
print("All the pin setup done")
>>>>>>> bc1409b55bf824af925a89f4d59e9bf53b415969

def callback(data):
    global max_pwm, turn_pwm move_pwm
    x = data.linear.x
    z = data.angular.z

    move_pwm = x * 50
    turn_pwm = x * 30

<<<<<<< HEAD
    # converting into duty cycle from the teleop message by mulitplying it to 10
    duty =( lin * 10)
=======
    if(move_pwm > max_pwm):
        move_pwm = max_pwm 
>>>>>>> bc1409b55bf824af925a89f4d59e9bf53b415969

    if(turn_pwm > max_pwm):
        turn_pwm = max_pwm 
    
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
    global max_pwm, turn_pwm move_pwm
    print("forward")
    p1.ChangeDutyCycle(move_pwm)
    p2.ChangeDutyCycle(move_pwm)
    GPIO.output(in1,GPIO.HIGH) # anti
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH) # clock
    GPIO.output(in4,GPIO.LOW)

def backward():
    global max_pwm, turn_pwm move_pwm
    print("backward")
    p1.ChangeDutyCycle(move_pwm)
    p2.ChangeDutyCycle(move_pwm)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def right():
    global max_pwm, turn_pwm move_pwm
    print("right turn")
    p1.ChangeDutyCycle(turn_pwm)
    p2.ChangeDutyCycle(turn_pwm)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def left():
    global max_pwm, turn_pwm move_pwm
    print("left  turn")
    p1.ChangeDutyCycle(turn_pwm)
    p2.ChangeDutyCycle(turn_pwm)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def stop():
    global max_pwm, turn_pwm move_pwm
    print("stop")  
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
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

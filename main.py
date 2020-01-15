# Main Python File for Testing Stepper motors with the TB 6600

import RPi.GPIO as GPIO
import time
import curses


QUICKDELAY = 0.0003 #Change this depends on your stepper motor
SLOWDELAY = 0.00045

# Change wiring here for your axis (in GPIO)
XDir = 6
XStepPin = 13
XEnable = 5
YDir = 27
YStepPin = 22
YEnable = 17
ZDir = 19
ZStepPin = 4
ZEnable = 26
SERVOPIN = 12

def motor_initialize(dir_pin, step_pin, en_pin):
    GPIO.setup(dir_pin, GPIO.OUT)
    GPIO.setup(step_pin, GPIO.OUT)
    GPIO.setup(en_pin, GPIO.OUT)
    GPIO.output(en_pin, GPIO.HIGH)
    GPIO.setup(SERVOPIN, GPIO.OUT)

    pass

def pulse_y_cw():
    for i in range(1000): 
        GPIO.output(YDir, 0) 
        GPIO.output(YStepPin, 1)
        time.sleep(delay)
        GPIO.output(YStepPin, 0)
        time.sleep(delay)
        print ("Moving Y CW \n")
    pass

def pulse_y_ccw():
    
    for i in range(1000): 
        GPIO.output(YDir, 1)
        GPIO.output(YStepPin, 1)
        time.sleep(delay)
        GPIO.output(YStepPin, 0)
        time.sleep(delay)
        print ("Moving Y CCW \n")
    pass

def pulse_x_cw():
    for i in range(5000): 
        GPIO.output(XDir, 0)
        GPIO.output(XStepPin, 1)
        time.sleep(delay)
        GPIO.output(XStepPin, 0)
        time.sleep(delay)
        print ("Moving X CCW \n")
    pass

def pulse_x_ccw():
    for i in range(5000): 
        GPIO.output(XDir, 1)
        GPIO.output(XStepPin, 1)
        time.sleep(delay)
        GPIO.output(XStepPin, 0)
        time.sleep(delay)
        print ("Moving X CCW \n")
    pass

def pulse_z_cw():
    for i in range(100): 
        GPIO.output(ZDir, 0)
        GPIO.output(ZStepPin, 1)
        time.sleep(SLOWDELAY)
        GPIO.output(ZStepPin, 0)
        time.sleep(SLOWDELAY)
        print ("Moving Z CW \n")
    pass


def pulse_z_ccw():
    for i in range(50): 
        GPIO.output(ZDir, 1)
        GPIO.output(ZStepPin, 1)
        time.sleep(SLOWDELAY)
        GPIO.output(ZStepPin, 0)
        time.sleep(SLOWDELAY)
        print ("Moving Z CCW \n")
    pass

def servo_left():
    global p
    p.ChangeDutyCycle(2.5)

def servo_right():
    global p
    p.ChangeDutyCycle(11.5)

def servo_stop(): 
    global p
    p.ChangeDutyCycle(7)

delay = QUICKDELAY

screen = curses.initscr()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
motor_initialize(XDir,XStepPin,XEnable)
motor_initialize(YDir,YStepPin,YEnable)
motor_initialize(ZDir,ZStepPin,ZEnable)
p = GPIO.PWM(SERVOPIN, 50)
p.start(5)
print("Initialized. Use the following keys for control\n")
print("WASD: controlling X and Y motors\n")
print("  QE: raising and lowering Z motor\n")
print("   X: to quit the program\n")

while True:
    c = screen.getch()
    time.sleep(0.03)
    if c == ord('w'):
        pulse_x_ccw()
    elif c == ord('s'):
        pulse_x_cw()
    elif c == ord('a'):
        pulse_y_ccw()
    elif c == ord('d'):
        pulse_y_cw()
    elif c == ord('q'):
        pulse_z_ccw()
    elif c == ord('e'):
        pulse_z_cw()
    elif c == ord('z'):
        servo_left()
    elif c == ord('c'):
        servo_right()
    elif c == ord('x'):
        servo_stop()
    elif c == ord('r'):
        break  # Exit the while loop


import RPi.GPIO as GPIO
import time
from motor import MOTOR
 
 
class FOLLOWER():
    def __init__(self, motor_left_pin1=17, motor_left_pin2=27, motor_right_pin1=23, motor_right_pin2=24,
                 line_follow_pin_left=19, line_follow_pin_right=6 ):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # init modules
        self.motor = L293D(motor_left_pin1, motor_left_pin2, motor_right_pin1, motor_right_pin2)
        self.line_follow_pin_left  = line_follow_pin_left
        self.line_follow_pin_right = line_follow_pin_right
        
        GPIO.setup(self.line_follow_pin_left,  GPIO.IN)
        GPIO.setup(self.line_follow_pin_right, GPIO.IN)
    
    def lineFollowModeOn(self):
     
        status_left  = False
        status_right = False
        
        while True:
            status_left  = bool(GPIO.input(self.line_follow_pin_left))  
            status_right = bool(GPIO.input(self.line_follow_pin_right)) 
            
            if status_left and status_right:
                self.motor.forward()
            elif status_left:
                self.motor.forwardR()
            elif status_right:
                self.motor.forwardL()
            else:
                self.motor.backward()
                time.sleep(7.5/self.motor.CM_PER_SEC)
                self.motor.stop()
                degrees_to_search = 45.0
                self.motor.forwardR()
                s = GPIO.wait_for_edge(self.line_follow_pin_left, GPIO.RISING, timeout=int(1000 * self.motor.SEC_PER_TURN / 360.0 * degrees_to_search))
                self.motor.stop()
                if s is not None:
                    continue
                else:
                    self.motor.backwardR()
                    time.sleep(self.motor.SEC_PER_TURN / 360.0 * degrees_to_search)
                    self.motor.forwardL()
                    s = GPIO.wait_for_edge(self.line_follow_pin_right, GPIO.RISING, timeout=int(1000 * self.motor.SEC_PER_TURN / 360.0 * degrees_to_search))
                    self.motor.stop()
                    if s is not None:
                        print("fund")
                        continue
                    else:
                        self.motor.backwardL()
                        time.sleep(self.motor.CM_PER_TURN / 360.0 * degrees_to_search)
                        self.motor.stop()
                        break
            time.sleep(0.001)
    

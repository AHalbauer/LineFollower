import RPi.GPIO as GPIO
import time
import threading

class MOTOR():
    CM_PER_SEC  = 35.0

    def __init__(self, left_pin1, left_pin2, right_pin1, right_pin2):
        self.MOTOR_LEFT_PIN1  = left_pin1
        self.MOTOR_LEFT_PIN2  = left_pin2
        self.MOTOR_RIGHT_PIN1 = right_pin1
        self.MOTOR_RIGHT_PIN2 = right_pin2

        GPIO.setup(self.MOTOR_LEFT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_LEFT_PIN2, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN2, GPIO.OUT)
        
    def forward(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
        return time.time()

    def forwardL(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        return time.time()

    def forwardR(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()
        
    def backward(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        return time.time()

    def backwardL(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()

    def backwardR(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()
        
    def stop(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)

import RPi.GPIO as GPIO
import time
from my_controller import MyController  # Import your PS4 controller class

# Define GPIO pins
PWM_LEFT = 18  # Example PWM pin for left motor
DIR_LEFT = 23  # Example Direction pin for left motor
PWM_RIGHT = 19  # Example PWM pin for right motor
DIR_RIGHT = 24  # Example Direction pin for right motor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_LEFT, GPIO.OUT)
GPIO.setup(DIR_LEFT, GPIO.OUT)
GPIO.setup(PWM_RIGHT, GPIO.OUT)
GPIO.setup(DIR_RIGHT, GPIO.OUT)

# Create PWM instances
pwm_left = GPIO.PWM(PWM_LEFT, 1000)  # 1 kHz frequency
pwm_right = GPIO.PWM(PWM_RIGHT, 1000)
pwm_left.start(0)  # Start with 0% duty cycle
pwm_right.start(0)

class MotorController(MyController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_L3_up(self, value):
        speed = abs(value) / 32767 * 100  # Normalize value to 0-100%
        GPIO.output(DIR_LEFT, GPIO.HIGH)
        GPIO.output(DIR_RIGHT, GPIO.HIGH)
        pwm_left.ChangeDutyCycle(speed)
        pwm_right.ChangeDutyCycle(speed)
        
    def on_L3_down(self, value):
        speed = abs(value) / 32767 * 100
        GPIO.output(DIR_LEFT, GPIO.LOW)
        GPIO.output(DIR_RIGHT, GPIO.LOW)
        pwm_left.ChangeDutyCycle(speed)
        pwm_right.ChangeDutyCycle(speed)

    def on_R3_left(self, value):
        speed = abs(value) / 32767 * 100
        GPIO.output(DIR_LEFT, GPIO.LOW)
        GPIO.output(DIR_RIGHT, GPIO.HIGH)
        pwm_left.ChangeDutyCycle(speed)
        pwm_right.ChangeDutyCycle(speed)

    def on_R3_right(self, value):
        speed = abs(value) / 32767 * 100
        GPIO.output(DIR_LEFT, GPIO.HIGH)
        GPIO.output(DIR_RIGHT, GPIO.LOW)
        pwm_left.ChangeDutyCycle(speed)
        pwm_right.ChangeDutyCycle(speed)

    def on_L3_x_at_rest(self):
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

    def on_L3_y_at_rest(self):
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

    def on_R3_x_at_rest(self):
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

    def on_R3_y_at_rest(self):
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

if __name__ == "__main__":
    try:
        controller = MotorController(interface="/dev/input/js0", connecting_using_ds4drv=False)
        controller.listen()
    except KeyboardInterrupt:
        print("Exiting...")
        pwm_left.stop()
        pwm_right.stop()
        GPIO.cleanup()

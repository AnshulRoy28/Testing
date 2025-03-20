import time
import RPi.GPIO as GPIO  # Use appropriate library for your hardware

# Define motor driver pins
PWM_PIN = 18  # Change according to your setup
DIR_PIN = 23  # Direction control pin

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set direction
GPIO.output(DIR_PIN, GPIO.HIGH)  # Change to GPIO.LOW for reverse

# Set up PWM
pwm = GPIO.PWM(PWM_PIN, 20000)  # 20KHz frequency
pwm.start(0)  # Start with 0% duty cycle

# Ramp speed from 0% to 100% over 3 seconds
duration = 3  # seconds
steps = 100  # Number of steps
step_delay = duration / steps

try:
    for duty_cycle in range(0, 101, 1):
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(step_delay)
finally:
    pwm.stop()
    GPIO.cleanup()

import time
import pigpio  # New recommended library for Raspberry Pi 5

# Define motor driver pins
PWM_PIN = 18  # Change according to your setup
DIR_PIN = 23  # Direction control pin

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    exit("Error: pigpio daemon not running.")

# Set up pins
pi.set_mode(PWM_PIN, pigpio.OUTPUT)
pi.set_mode(DIR_PIN, pigpio.OUTPUT)

# Set direction
pi.write(DIR_PIN, 1)  # Set HIGH for forward, LOW for reverse

# Ramp speed from 0% to 100% over 3 seconds
duration = 3  # seconds
steps = 100  # Number of steps
step_delay = duration / steps

try:
    for duty_cycle in range(0, 101, 1):
        pwm_value = int((duty_cycle / 100) * 255)  # Scale to 8-bit (0-255)
        pi.set_PWM_dutycycle(PWM_PIN, pwm_value)
        time.sleep(step_delay)
finally:
    pi.set_PWM_dutycycle(PWM_PIN, 0)  # Stop PWM
    pi.stop()  # Clean up

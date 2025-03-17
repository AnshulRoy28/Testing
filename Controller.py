from pyPS4Controller.controller import Controller

class VehicleController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = "motion"  # Initial mode: motion or pump
        self.arm_position = 0  # Arm position (0 = neutral, positive = raised, negative = lowered)
        self.l2_suction = False  # Left vacuum suction state
        self.r2_suction = False  # Right vacuum suction state
        self.dead_zone = 1000  # Dead zone for joystick drift

        # Store last valid joystick values
        self.last_l3_y_value = 0  # Forward/backward movement
        self.last_r3_x_value = 0  # Left/right rotation

    def apply_dead_zone(self, value):
        """Ignore small movements to reduce drift."""
        return value if abs(value) > self.dead_zone else 0

    # L3 Joystick (Forward and Backward Movement)
    def on_L3_up(self, value):
        """Handle forward movement."""
        value = self.apply_dead_zone(value)
        if value:
            self.last_l3_y_value = value
            print(f"Moving Forward: {value}")
        elif self.last_l3_y_value != 0:
            print(f"Using Last Forward Value: {self.last_l3_y_value}")

    def on_L3_down(self, value):
        """Handle backward movement."""
        value = self.apply_dead_zone(value)
        if value:
            self.last_l3_y_value = -value
            print(f"Moving Backward: {value}")
        elif self.last_l3_y_value != 0:
            print(f"Using Last Backward Value: {self.last_l3_y_value}")

    def on_L3_y_at_rest(self):
        """L3 y-axis at rest."""
        self.last_l3_y_value = 0
        print("L3 Y-Axis at Rest: Stopping Movement")

    # R3 Joystick (Left and Right Rotation)
    def on_R3_left(self, value):
        """Handle left rotation."""
        value = self.apply_dead_zone(value)
        if value:
            self.last_r3_x_value = -value
            print(f"Rotating Left: {value}")
        elif self.last_r3_x_value != 0:
            print(f"Using Last Left Rotation Value: {self.last_r3_x_value}")

    def on_R3_right(self, value):
        """Handle right rotation."""
        value = self.apply_dead_zone(value)
        if value:
            self.last_r3_x_value = value
            print(f"Rotating Right: {value}")
        elif self.last_r3_x_value != 0:
            print(f"Using Last Right Rotation Value: {self.last_r3_x_value}")

    def on_R3_x_at_rest(self):
        """R3 x-axis at rest."""
        self.last_r3_x_value = 0
        print("R3 X-Axis at Rest: Stopping Rotation")

    # Triangle Button (Switch Modes)
    def on_triangle_press(self):
        self.mode = "pump" if self.mode == "motion" else "motion"
        print(f"Switched to {self.mode.capitalize()} Mode")

    def on_triangle_release(self):
        print("Triangle Button Released")

    # Up/Down Buttons (Raise/Lower Arm)
    def on_up_arrow_press(self):
        self.arm_position += 1
        print(f"Raising Arm to Position: {self.arm_position}")

    def on_up_down_arrow_release(self):
        print("Up/Down Arrow Released")

    def on_down_arrow_press(self):
        self.arm_position -= 1
        print(f"Lowering Arm to Position: {self.arm_position}")

    # L2/R2 Triggers (Left/Right Vacuum Suction)
    def on_L2_press(self, value):
        self.l2_suction = True
        print("Left Vacuum Suction Activated")

    def on_L2_release(self):
        self.l2_suction = False
        print("Left Vacuum Suction Deactivated")

    def on_R2_press(self, value):
        self.r2_suction = True
        print("Right Vacuum Suction Activated")

    def on_R2_release(self):
        self.r2_suction = False
        print("Right Vacuum Suction Deactivated")

    # Additional Buttons (Optional)
    def on_x_press(self):
        print("X Button Pressed")

    def on_x_release(self):
        print("X Button Released")

    def on_circle_press(self):
        print("Circle Button Pressed")

    def on_circle_release(self):
        print("Circle Button Released")

    def on_square_press(self):
        print("Square Button Pressed")

    def on_square_release(self):
        print("Square Button Released")

    def on_L1_press(self):
        print("L1 Button Pressed")

    def on_L1_release(self):
        print("L1 Button Released")

    def on_R1_press(self):
        print("R1 Button Pressed")

    def on_R1_release(self):
        print("R1 Button Released")

    def on_options_press(self):
        print("Options Button Pressed")

    def on_options_release(self):
        print("Options Button Released")

    def on_share_press(self):
        print("Share Button Pressed")

    def on_share_release(self):
        print("Share Button Released")

    def on_playstation_button_press(self):
        print("PlayStation Button Pressed")

    def on_playstation_button_release(self):
        print("PlayStation Button Released")


if __name__ == "__main__":
    controller = VehicleController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

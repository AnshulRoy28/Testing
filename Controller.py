from pyPS4Controller.controller import Controller

class VehicleController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = "motion"  # Initial mode: motion or pump
        self.arm_position = 0  # Arm position (0 = neutral, positive = raised, negative = lowered)
        self.l2_suction = False  # Left vacuum suction state
        self.r2_suction = False  # Right vacuum suction state
        self.dead_zone = 1000  # Dead zone for joystick drift

    def apply_dead_zone(self, value):
        """Ignore small movements to reduce drift."""
        return value if abs(value) > self.dead_zone else 0

    # L3 Joystick (Forward and Backward Movement)
    def on_L3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"Moving Forward: {value}")
        else:
            print("Stopping Forward Movement")

    def on_L3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"Moving Backward: {value}")
        else:
            print("Stopping Backward Movement")

    def on_L3_y_at_rest(self):
        """L3 y-axis at rest."""
        print("L3 Y-Axis at Rest")

    # R3 Joystick (Left and Right Rotation)
    def on_R3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"Rotating Left: {value}")
        else:
            print("Stopping Left Rotation")

    def on_R3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"Rotating Right: {value}")
        else:
            print("Stopping Right Rotation")

    def on_R3_x_at_rest(self):
        """R3 x-axis at rest."""
        print("R3 X-Axis at Rest")

    # Triangle Button (Switch Modes)
    def on_triangle_press(self):
        self.mode = "pump" if self.mode == "motion" else "motion"
        print(f"Switched to {self.mode.capitalize()} Mode")

    # Up Button (Raise Arm)
    def on_up_arrow_press(self):
        self.arm_position += 1
        print(f"Raising Arm to Position: {self.arm_position}")

    # Down Button (Lower Arm)
    def on_down_arrow_press(self):
        self.arm_position -= 1
        print(f"Lowering Arm to Position: {self.arm_position}")

    # L2 Trigger (Left Vacuum Suction)
    def on_L2_press(self, value):
        self.l2_suction = True
        print("Left Vacuum Suction Activated")

    def on_L2_release(self):
        self.l2_suction = False
        print("Left Vacuum Suction Deactivated")

    # R2 Trigger (Right Vacuum Suction)
    def on_R2_press(self, value):
        self.r2_suction = True
        print("Right Vacuum Suction Activated")

    def on_R2_release(self):
        self.r2_suction = False
        print("Right Vacuum Suction Deactivated")


if __name__ == "__main__":
    controller = VehicleController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

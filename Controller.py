from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = "Motion"  # Default mode
        self.dead_zone = 1000  # Adjust this value based on your controller drift

    def apply_dead_zone(self, value):
        """Ignore small movements to reduce drift."""
        return value if abs(value) > self.dead_zone else 0

    # L3 Joystick (Movement)
    def on_L3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"L3 Moving Forward: {value}")
        return value

    def on_L3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"L3 Moving Backward: {value}")
        return value

    def on_L3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"L3 Moving Left: {value}")
        return value

    def on_L3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"L3 Moving Right: {value}")
        return value

    # R3 Joystick (Rotation)
    def on_R3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"R3 Looking Up: {value}")
        return value

    def on_R3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"R3 Looking Down: {value}")
        return value

    def on_R3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"R3 Rotating Left: {value}")
        return value

    def on_R3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            print(f"R3 Rotating Right: {value}")
        return value

    # Triangle Button - Switch Mode
    def on_triangle_press(self):
        self.mode = "Pump" if self.mode == "Motion" else "Motion"
        print(f"Mode switched to: {self.mode}")
        return self.mode

    # D-pad Up & Down (Raise & Lower Arm)
    def on_up_arrow_press(self):
        print("Raising Arm")
        return "Raising Arm"

    def on_down_arrow_press(self):
        print("Lowering Arm")
        return "Lowering Arm"

    # L2 (Left Vacuum Suction)
    def on_L2_press(self):
        print("Left Vacuum Suction Activated")
        return "L2 Pressed"

    # R2 (Right Vacuum Suction)
    def on_R2_press(self):
        print("Right Vacuum Suction Activated")
        return "R2 Pressed"

if __name__ == "__main__":
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = "Motion"  # Default mode

        # Define ignored drift values for each joystick direction
        self.ignored_l3_up = {-775, -259, -1033, -517}
        self.ignored_l3_down = {-775,774,516,258, -259, -1033, -517}
        self.ignored_l3_left = {-1549,-517, -1807, -775, -1033}
        self.ignored_l3_right = {1548,1290, 1807,516,258, 774, 1032}

        self.ignored_r3_up = {-775, -259, -1033, -517}
        self.ignored_r3_down = {-775, -259, -1033, -517}
        self.ignored_r3_left = {-1549, -1807, -775, -1033}
        self.ignored_r3_right = {1032,1806, 774,1548, 2064, 2322, 1290}

    # L3 Joystick (Movement)
    def on_L3_up(self, value):
        if value in self.ignored_l3_up:
            return
        print(f"L3 Moving Forward: {value}")
        return value

    def on_L3_down(self, value):
        if value in self.ignored_l3_down:
            return
        print(f"L3 Moving Backward: {value}")
        return value

    def on_L3_left(self, value):
        if value in self.ignored_l3_left:
            return
        print(f"L3 Moving Left: {value}")
        return value

    def on_L3_right(self, value):
        if value in self.ignored_l3_right:
            return
        print(f"L3 Moving Right: {value}")
        return value

    # R3 Joystick (Rotation)
    def on_R3_up(self, value):
        if value in self.ignored_r3_up:
            return
        print(f"R3 Looking Up: {value}")
        return value

    def on_R3_down(self, value):
        if value in self.ignored_r3_down:
            return
        print(f"R3 Looking Down: {value}")
        return value

    def on_R3_left(self, value):
        if value in self.ignored_r3_left:
            return
        print(f"R3 Rotating Left: {value}")
        return value

    def on_R3_right(self, value):
        if value in self.ignored_r3_right:
            return
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

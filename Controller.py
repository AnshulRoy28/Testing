from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dead_zone = 1000  # Ignore small drift values
        self.l3_active = False  # Track if joystick is being held
        self.r3_active = False

    def apply_dead_zone(self, value):
        """Ignore small movements to reduce drift."""
        return value if abs(value) > self.dead_zone else 0

    # L3 Joystick (Movement)
    def on_L3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            print(f"L3 Moving Forward: {value}")
        else:
            self.l3_active = False
            print("L3 Stopped Moving Forward")

    def on_L3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            print(f"L3 Moving Backward: {value}")
        else:
            self.l3_active = False
            print("L3 Stopped Moving Backward")

    def on_L3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            print(f"L3 Moving Left: {value}")
        else:
            self.l3_active = False
            print("L3 Stopped Moving Left")

    def on_L3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            print(f"L3 Moving Right: {value}")
        else:
            self.l3_active = False
            print("L3 Stopped Moving Right")

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest (centered)."""
        self.l3_active = False
        print("L3 Joystick at Rest")

    def on_L3_y_at_rest(self):
        self.l3_active = False
        print("L3 Joystick at Rest")

    # R3 Joystick (Rotation)
    def on_R3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            print(f"R3 Looking Up: {value}")
        else:
            self.r3_active = False
            print("R3 Stopped Looking Up")

    def on_R3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            print(f"R3 Looking Down: {value}")
        else:
            self.r3_active = False
            print("R3 Stopped Looking Down")

    def on_R3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            print(f"R3 Rotating Left: {value}")
        else:
            self.r3_active = False
            print("R3 Stopped Rotating Left")

    def on_R3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            print(f"R3 Rotating Right: {value}")
        else:
            self.r3_active = False
            print("R3 Stopped Rotating Right")

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest (centered)."""
        self.r3_active = False
        print("R3 Joystick at Rest")

    def on_R3_y_at_rest(self):
        self.r3_active = False
        print("R3 Joystick at Rest")


if __name__ == "__main__":
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

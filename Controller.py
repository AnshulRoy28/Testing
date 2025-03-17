from pyPS4Controller.controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dead_zone = 1000  # Ignore small drift values
        self.l3_active = False  # Track if joystick is being held
        self.r3_active = False
        self.last_l3_x_value = 0  # Store the last valid L3 x-axis value
        self.last_l3_y_value = 0  # Store the last valid L3 y-axis value
        self.last_r3_x_value = 0  # Store the last valid R3 x-axis value
        self.last_r3_y_value = 0  # Store the last valid R3 y-axis value

    def apply_dead_zone(self, value):
        """Ignore small movements to reduce drift."""
        return value if abs(value) > self.dead_zone else 0

    # L3 Joystick (Movement)
    def on_L3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            self.last_l3_y_value = value
            print(f"L3 Moving Forward: {value}")
        else:
            self.l3_active = False
            print(f"L3 Using Last Value Forward: {self.last_l3_y_value}")

    def on_L3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            self.last_l3_y_value = -value
            print(f"L3 Moving Backward: {value}")
        else:
            self.l3_active = False
            print(f"L3 Using Last Value Backward: {self.last_l3_y_value}")

    def on_L3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            self.last_l3_x_value = -value
            print(f"L3 Moving Left: {value}")
        else:
            self.l3_active = False
            print(f"L3 Using Last Value Left: {self.last_l3_x_value}")

    def on_L3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.l3_active = True
            self.last_l3_x_value = value
            print(f"L3 Moving Right: {value}")
        else:
            self.l3_active = False
            print(f"L3 Using Last Value Right: {self.last_l3_x_value}")

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest (centered)."""
        self.l3_active = False
        print(f"L3 Joystick at Rest, Using Last Value X: {self.last_l3_x_value}")

    def on_L3_y_at_rest(self):
        self.l3_active = False
        print(f"L3 Joystick at Rest, Using Last Value Y: {self.last_l3_y_value}")

    # R3 Joystick (Rotation)
    def on_R3_up(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            self.last_r3_y_value = value
            print(f"R3 Looking Up: {value}")
        else:
            self.r3_active = False
            print(f"R3 Using Last Value Up: {self.last_r3_y_value}")

    def on_R3_down(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            self.last_r3_y_value = -value
            print(f"R3 Looking Down: {value}")
        else:
            self.r3_active = False
            print(f"R3 Using Last Value Down: {self.last_r3_y_value}")

    def on_R3_left(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            self.last_r3_x_value = -value
            print(f"R3 Rotating Left: {value}")
        else:
            self.r3_active = False
            print(f"R3 Using Last Value Left: {self.last_r3_x_value}")

    def on_R3_right(self, value):
        value = self.apply_dead_zone(value)
        if value:
            self.r3_active = True
            self.last_r3_x_value = value
            print(f"R3 Rotating Right: {value}")
        else:
            self.r3_active = False
            print(f"R3 Using Last Value Right: {self.last_r3_x_value}")

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest (centered)."""
        self.r3_active = False
        print(f"R3 Joystick at Rest, Using Last Value X: {self.last_r3_x_value}")

    def on_R3_y_at_rest(self):
        self.r3_active = False
        print(f"R3 Joystick at Rest, Using Last Value Y: {self.last_r3_y_value}")


if __name__ == "__main__":
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

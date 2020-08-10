from pygame import joystick

import joymenu.game as game
import joymenu.reactive


class XboxController:
    threshold = 0.9
    buttons = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'BACK', 'START', 'XBOX', 'L3', 'R3', '?']
    axis = ['LX', 'LY', 'LT', 'RX', 'RY', 'RT']
    hats = ['ARROWS']


class InputHandler:
    def __init__(self, reactive_broker: joymenu.reactive.ReactiveBroker):
        self.reactive_broker = reactive_broker
        self._controller = XboxController()
        self._init_available_joysticks()

    @staticmethod
    def _init_available_joysticks():
        for j in range(joystick.get_count()):
            joystick.Joystick(j).init()

    def handle_button_input(self, event):
        # print(f"Event{event}")
        if self._controller.buttons[event.button] == 'A':
            self.reactive_broker.register(self.reactive_broker.SELECT)

    def handle_analog_input(self, event):
        # print(f"\t\tEixo analogico ou gatilho ({self._controller.axis[event.axis]}): {event.value}")
        if self._controller.axis[event.axis] in ['LX', 'RX']:
            if self._is_meaningful(event):
                self._get_sense(event.value)

    def _is_meaningful(self, event):
        return abs(event.value) >= self._controller.threshold

    def handle_hat_input(self, event):
        #print(f"{self._controller.hats[event.hat]}: {event.value}")
        x, _ = event.value
        self._get_sense(x)

    def _get_sense(self, value):
        if value < 0:
            self.reactive_broker.register(self.reactive_broker.BACKWARD)
        elif value > 0:
            self.reactive_broker.register(self.reactive_broker.FORWARD)

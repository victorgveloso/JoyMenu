import pygame
from pygame import joystick

import joymenu.reactive


class XboxController:
    threshold = 0.9
    buttons = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'BACK', 'START', 'XBOX', 'L3', 'R3', '?']
    axis = ['LX', 'LY', 'LT', 'RX', 'RY', 'RT']
    hats = ['ARROWS']


class KeyboardController:
    class KeyboardKey:
        def __init__(self, type_, value=None):
            self.type = type_
            self.value = value

    ARROWS = "ARROWS"
    ENTER = "ENTER"
    keys = {
        275: KeyboardKey(ARROWS, 1),
        276: KeyboardKey(ARROWS, -1),
        13: KeyboardKey(ENTER)
    }


class InputHandler:
    def __init__(self, reactive_broker: joymenu.reactive.ReactiveBroker):
        self.reactive_broker = reactive_broker
        self.init_available_joysticks()

    @staticmethod
    def init_available_joysticks():
        for j in range(joystick.get_count()):
            j = joystick.Joystick(j)
            j.quit()
            j.init()

    @staticmethod
    def restart_joystick(j: joystick.Joystick, tried=0):
        try:
            j.quit()
            j.init()
        except pygame.error:
            tried += 1
            if tried < 5:
                InputHandler.restart_joystick(j, tried)

    def handle_button_input(self, event):
        # print(f"Event{event}")
        if XboxController.buttons[event.button] == 'A':
            self.reactive_broker.register(self.reactive_broker.SELECT)

    def handle_analog_input(self, event):
        # print(f"\t\tEixo analogico ou gatilho ({XboxController.axis[event.axis]}): {event.value}")
        if XboxController.axis[event.axis] in ['LX', 'RX']:
            if self._is_meaningful(event):
                self._get_sense(event.value)

    def _is_meaningful(self, event):
        return abs(event.value) >= XboxController.threshold

    def handle_hat_input(self, event):
        # print(f"{XboxController.hats[event.hat]}: {event.value}")
        x, _ = event.value
        self._get_sense(x)

    def handle_keyboard_input(self, event):
        try:
            key = KeyboardController.keys[event.key]
        except KeyError:
            return

        if key.type == KeyboardController.ARROWS:
            self._get_sense(key.value)
        elif key.type == KeyboardController.ENTER:
            self.reactive_broker.register(self.reactive_broker.SELECT)

    def _get_sense(self, value):
        if value < 0:
            self.reactive_broker.register(self.reactive_broker.BACKWARD)
        elif value > 0:
            self.reactive_broker.register(self.reactive_broker.FORWARD)

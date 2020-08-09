from pygame import joystick as joystick


class XboxController:
    threshold = 0.9
    buttons = ['A', 'B', 'X', 'Y', 'LB', 'RB', 'BACK', 'START', 'XBOX', 'L3', 'R3', '?']
    axis = ['LX', 'LY', 'LT', 'RX', 'RY', 'RT']
    hats = ['ARROWS']


class InputHandler:
    def __init__(self):
        self._controller = XboxController()
        self._init_available_joysticks()

    @staticmethod
    def _init_available_joysticks():
        for j in range(joystick.get_count()):
            joystick.Joystick(j).init()

    def handle_button_input(self, event):
        print(f"\t\tBotao: {self._controller.buttons[event.button]}")
        if self._controller.buttons[event.button] == 'A':
            print('Selecionar')

    def handle_analog_input(self, event):
        print(f"\t\tEixo analogico ou gatilho ({self._controller.axis[event.axis]}): {event.value}")
        if self._controller.axis[event.axis] in ['LX', 'RX']:
            if self._is_meaningful(event):
                self._get_sense(event.value)

    def _is_meaningful(self, event):
        return abs(event.value) >= self._controller.threshold

    def handle_hat_input(self, event):
        print(f"{self._controller.hats[event.hat]}: {event.value}")
        x, _ = event.value
        self._get_sense(x)

    @staticmethod
    def _get_sense(value):
        if value < 0:
            print('Anterior')
        elif value > 0:
            print('Próximo')

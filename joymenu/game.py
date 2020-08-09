from typing import Tuple

import pygame

import joymenu.menuentries as menuentries
import pygame.image as image
import joymenu.controllers as controllers


class MenuView:
    def __init__(self, game, entries: menuentries.MenuEntries, screen_res: Tuple[int, int]):
        self.input_handler = controllers.InputHandler()
        self.size = 250
        self._icons = self.load_resized_images(entries)
        self._game = game
        self.x_pos, self.y_pos = self.get_starting_pos(entries, screen_res)

    def load_resized_images(self, entries):
        return [self.resize_image(pygame.image.load(entry.icon)) for entry in entries.values]

    def get_starting_pos(self, entries, screen_res):
        screen_width, screen_height = screen_res
        menu_width = (self.size * len(entries))
        menu_height = self.size
        x = (screen_width - menu_width) / 2
        y = (screen_height - menu_height) / 2
        return x, y

    def draw(self):
        threshold = 0
        for i in self._icons:
            self._game.frame.blit(i, (self.x_pos + threshold, self.y_pos))
            threshold += self.size

    def resize_image(self, i):
        return pygame.transform.scale(i, (self.size, self.size))

    def handle_input(self, event) -> bool:
        if event.type == pygame.JOYHATMOTION:
            self.input_handler.handle_hat_input(event)
        if event.type == pygame.JOYAXISMOTION:
            self.input_handler.handle_analog_input(event)
        if event.type == pygame.JOYBUTTONDOWN:
            self.input_handler.handle_button_input(event)
        return True


class Game:
    WHITE = (255, 255, 255)
    DEFAULT_RES = (800, 600)

    def __init__(self, entries):
        self.entries = entries

        pygame.init()

        self.screen = pygame.display
        self.max_res = self._get_screen_res()
        self.menu = MenuView(self, entries, self.max_res)
        self.frame = self.screen.set_mode(self.DEFAULT_RES)
        self.is_fullscreen = False

    def main_loop(self):
        should_continue = True
        while should_continue:
            for ev in pygame.event.get():
                should_continue = should_continue and self._handle_input(ev)
            self._draw_frame()
            self.screen.update()

    def _draw_frame(self):
        self.frame.fill(self.WHITE)
        self.menu.draw()

    def _handle_input(self, event):
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._toggle_mode()
                return True
        return self.menu.handle_input(event)

    def _get_screen_res(self) -> Tuple[int, int]:
        screen_res = self.screen.Info()
        return screen_res.current_w, screen_res.current_h

    def _toggle_mode(self):
        if not self.is_fullscreen:
            self.frame = self.screen.set_mode(self.max_res, pygame.FULLSCREEN | pygame.DOUBLEBUF)
        else:
            self.frame = self.screen.set_mode(self.DEFAULT_RES)
        self.is_fullscreen = not self.is_fullscreen

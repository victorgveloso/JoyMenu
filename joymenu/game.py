from typing import Tuple

import pygame

import joymenu.menuentries as menuentries


class MenuView:
    def __init__(self, game, entries: menuentries.MenuEntries):
        self._icons = []
        for entry in entries.values:
            self._icons.append(pygame.image.load(entry.icon))
        self._game = game

    def draw(self):
        summer = 0
        start = (400, 540)
        for i in self._icons:
            self._game.frame.blit(i, (start[0] + summer, start[1]))
            summer += 500

    def handle_input(self, event) -> bool:
        return True


class Game:
    WHITE = (255, 255, 255)
    DEFAULT_RES = (800, 600)

    def __init__(self, entries):
        self.entries = entries

        self.menu = MenuView(self, entries)

        pygame.init()

        self.screen = pygame.display
        self.max_res = self._get_screen_res()
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
            else:
                print(event)
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

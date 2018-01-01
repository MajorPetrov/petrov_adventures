#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: Vladimir Razdobreev

:date: 2017, december


Main game file - the main program loop

Petrov_against_cosmopolitans - platform game

"""

from os import path
from map import *
from sprites import *


class Game:
    def __init__(self):
        """
        Initialize game window
        """
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.running = True

    def load_data(self):
        folder = path.dirname(__file__)
        self.map = Map(path.join(folder, "level_1"))

    def new(self):
        """
        Start a new game
        :return: None
        """
        self.load_data()

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    p = Platform(col, row)
                    self.all_sprites.add(p)
                    self.platforms.add(p)

                elif tile == "p":
                    self.player = Player(self, col, row)  # parameter self make a link between the game and the player
                    self.all_sprites.add(self.player)

        self.camera = Camera(self.map.width, self.map.height)

        self.run()

    def run(self):
        """
        Game loop
        :return: None
        """
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)  # keep loop running at the right speed
            self.events()
            self.update()
            self.draw()

    def update(self):
        """
        Game loop - update (collision check)
        :return: None
        """
        self.all_sprites.update()
        self.camera.update(self.player)

        print(self.player.rect.bottom)

        # dying
        if self.player.rect.bottom > HEIGHT:
            self.playing = False

    def events(self):
        """
        Game loop - Process input (events)
        :return: None
        """
        for event in pygame.event.get():

            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.go_left()
                if event.key == pygame.K_RIGHT:
                    self.player.go_right()
                if event.key == pygame.K_SPACE:
                    self.player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()

    def draw(self):
        """
        Game loop - draw / render
        :return: None
        """
        self.screen.fill(BLACK)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        # after drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        """
        Game splash / start screen
        :return: None
        """
        pass

    def show_go_screen(self):
        """
        Game over / continue screen
        :return: None
        """
        pass

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()

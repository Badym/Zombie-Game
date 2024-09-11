from http.client import TEMPORARY_REDIRECT
from typing import NoReturn
from typing_extensions import NotRequired
import pygame
import random
from player import Player
from instance import Instance


import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400



class Game_Map():
    def __init__(self, name):
        self.player = Player(1600, 1200, 0.3, 5, 100, name) # JEDENGP
        self.hord = Instance(self.player)
        self.wave_mumber = 0
        gras_image = pygame.image.load('gras.png')

        dirt_image = pygame.image.load('ground5.png')

        # Pobierz rozmiary obrazka
        self.tile_width, self.tile_height = gras_image.get_size()

        self.mapa_img = [[None for _ in range(world_width // self.tile_width)] for _ in range(world_height // self.tile_height)]

        for y in range(0, world_height, self.tile_height):
            for x in range(0, world_width, self.tile_width):
                if random.randint(0, 1):
                    z = gras_image
                else:
                    z = dirt_image
                if random.randint(0, 400) == 44:
                    self.hord.spawn_box(x,y)
                self.mapa_img[y // self.tile_height][x // self.tile_width] = z



    def update(self,screen):
        print(self.player.max_hp)
        for y in range(0, world_height, self.tile_height):
            for x in range(0, world_width, self.tile_width):
                screen.blit(self.mapa_img[y // self.tile_height][x // self.tile_width], (x - self.player.offset_x, y - self.player.offset_y))

        for i in self.player.bullets:
            i.update(self.hord)
            i.draw(screen)

        self.hord.update(screen)

        if len(self.hord.enemyss) == 1:
            self.hord.fala(self.wave_mumber,self.wave_mumber,self.wave_mumber)
            self.wave_mumber += 1
            self.player.coins += self.wave_mumber + 10
            print("boxy: ",len(self.hord.boxes),",     enemys: ",len(self.hord.enemyss))

        if self.player.hp <= 0:
            return True
        return False





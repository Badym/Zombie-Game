from http.client import TEMPORARY_REDIRECT
from typing import NoReturn
from typing_extensions import NotRequired
import pygame
import random
from Enemy import Enemy
from Runner import Runner
from player import Player
from hp_box import Hp_Box
from ammo_box import Ammo_Box
from Wall import Wall
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400



class Instance():
    def __init__(self,player):
        self.player = player
        self.entities = pygame.sprite.Group()
        self.entities.add(player) 
        self.boxes = pygame.sprite.Group()
        d = Wall(300,300,1,0,120,self.player)
        self.entities.add(d)
        self.enemyss = pygame.sprite.Group()
        self.enemyss.add(player) 

    def fala(self,nr_enemy,nr_runner,nr_boxes):
        for i in range(0,nr_enemy):
            b = Enemy(random.randint(1, world_width), random.randint(1, world_height), 0.35, 2,100, self.player,self.entities)
            self.entities.add(b)
            self.enemyss.add(b)

        for i in range(0,nr_runner):
            c = Runner(random.randint(1, world_width), random.randint(1, world_height), 1, 1,100, self.player,self.entities)
            self.entities.add(c)
            self.enemyss.add(b)

        for i in range(0,nr_boxes):
            if random.randint(0,1):
                n = Hp_Box(random.randint(1, world_width), random.randint(1, world_height), 0.3, self.player)
            else:
                n = Ammo_Box(random.randint(1, world_width), random.randint(1, world_height), 0.3, self.player)
            self.boxes.add(n)

        


    def update(self,screen):
        for i in self.entities:
            i.update(screen)
            i.draw(screen)
            for zombie in self.entities:
                if zombie != self:
                    if i.rect.colliderect(zombie.rect):
                        # Wybierz kierunek, w którym zombie powinno siê poruszyæ, aby unikn¹æ kolizji
                        dx = i.rect.centerx - zombie.rect.centerx
                        dy = i.rect.centery - zombie.rect.centery
                        distance = math.sqrt(dx ** 2 + dy ** 2)
                        if distance != 0:
                            dx /= distance
                            dy /= distance
                        i.rect.x += dx * i.speed
                        i.rect.y += dy * i.speed

        for i in self.boxes:
            i.update(screen)
            i.draw(screen)

    def spawn_box(self,x,y):
        d = Wall(x,y,1,0,120,self.player)
        self.entities.add(d)


from http.client import TEMPORARY_REDIRECT
from entity import Entity
import pygame
import math
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400


class Wall(Entity,pygame.sprite.Sprite):
    def __init__(self,x,y,z,speed,hp,player):
        Entity.__init__(self, z,speed,hp)
        pygame.sprite.Sprite.__init__(self)

        self.animated_list.append(self.adding_animation(15,"Wall"))
        self.image = self.animated_list[self.index_anim][self.index_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.player = player

    def update(self,screen):
        self.up_animation()
        
    def draw(self, screen):
        screen.blit(pygame.transform.rotate(self.image, 0),(self.rect.x - self.player.offset_x, self.rect.y - self.player.offset_y))

    def adding_animation(self,size,nazwa_folderu):
        temp_list =[]
        for i in range(size):
            img = pygame.image.load(f'{nazwa_folderu}/{i}.png')
            if i > 8:
                img = pygame.transform.scale(img,(int((img.get_width())*self.scale*2),int((img.get_height())*(self.scale*2))))
            else:
                img = pygame.transform.scale(img,(int((img.get_width())*self.scale),int((img.get_height())*self.scale)))
            temp_list.append(img)
        return temp_list

    def up_animation(self):
        if self.hp <= 0:
            cooldown = 50
            if pygame.time.get_ticks() - self.current_time > cooldown:
                self.current_time = pygame.time.get_ticks()
                self.index_frame += 1
            if len(self.animated_list[self.index_anim]) <= self.index_frame:
                self.index_frame -=1
                self.player.max_hp += 10
                self.kill()

            self.image = self.animated_list[self.index_anim][self.index_frame]

    def delhp(self,dmg):
        self.hp -= dmg
        if self.hp <= 0:
            #self.kill()
            self.player.points += 8

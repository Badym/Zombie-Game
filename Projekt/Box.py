from http.client import TEMPORARY_REDIRECT
import pygame
from abc import ABC, abstractmethod


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,home):
        self.scale = scale
        self.player = home
    @abstractmethod
    def update(self,screen):
        pass
    @abstractmethod
    def draw(self, screen):
        pass

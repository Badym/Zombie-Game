from http.client import TEMPORARY_REDIRECT
from abc import ABC, abstractmethod
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60


class Entity(ABC):
    def __init__(self,z,speed,hp):
        self.scale = z
        self.direction = 0
        self.Flip_x = False
        self.rotation = 0
        self.current_time = pygame.time.get_ticks()
        self.index_anim = 0
        self.index_frame = 0
        self.animated_list =[]
        self.speed = speed
        self.max_hp = hp
        self.hp = hp

    @abstractmethod
    def adding_animation(self,size,nazwa_folderu):
        pass

    @abstractmethod
    def up_animation(self):
        pass
    @abstractmethod
    def update(self,screen):
        pass
    @abstractmethod
    def draw(self, screen):
        pass

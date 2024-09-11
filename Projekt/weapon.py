import pygame
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self,player):
        self.player = player


    @abstractmethod
    def set(self):
        pass

    @abstractmethod
    def shoot(self):
        pass



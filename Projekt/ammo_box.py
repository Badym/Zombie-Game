from http.client import TEMPORARY_REDIRECT
import pygame
from Box import Box 


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60

class Ammo_Box(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,home):
        pygame.sprite.Sprite.__init__(self)
        Box.__init__(self,x,y,scale,home)
        self.image = pygame.image.load(f'ammo_box/0.png')
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width()*self.scale),int(self.image.get_height()*self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def update(self,screen):
        if self.rect.colliderect(self.player.rect):
            self.player.ammo += 20
            self.kill()

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x - self.player.offset_x, self.rect.y - self.player.offset_y))
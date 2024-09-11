import pygame
from bullet import Bullet
from weapon import Weapon

class Pistol(Weapon):
    def __init__(self,player):
        Weapon.__init__(self,player)

    def set(self):
        self.player.shoot_cooldown = 20
        self.player.dmg = self.player.power

    def shoot(self):
        bull = Bullet(self.player.rect.centerx,self.player.rect.centery,1,8,0,self.player.direction,self.player)
        #self.bullet_gr.append(bull)
        self.player.bullets.add(bull)
        self.player.ammo-=1


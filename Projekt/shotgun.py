import pygame
from bullet import Bullet
from weapon import Weapon

class Shotgun(Weapon):
    def __init__(self,player):
        Weapon.__init__(self,player)

    def set(self):
        self.player.shoot_cooldown = 40
        self.player.dmg = self.player.power * 1.1

    def shoot(self):

        if self.player.direction <=1:
            bull1 = Bullet(self.player.rect.centerx,self.player.rect.centery+18,1,9,0,self.player.direction,self.player)
            bull2 = Bullet(self.player.rect.centerx,self.player.rect.centery,1,9,0,self.player.direction,self.player)
            bull3 = Bullet(self.player.rect.centerx,self.player.rect.centery-18,1,9,0,self.player.direction,self.player)
        else:
            bull1 = Bullet(self.player.rect.centerx+18,self.player.rect.centery,1,9,0,self.player.direction,self.player)
            bull2 = Bullet(self.player.rect.centerx,self.player.rect.centery,1,9,0,self.player.direction,self.player)
            bull3 = Bullet(self.player.rect.centerx-18,self.player.rect.centery,1,9,0,self.player.direction,self.player)

        #self.bullet_gr.append(bull)
        self.player.bullets.add(bull1)
        self.player.bullets.add(bull2)
        self.player.bullets.add(bull3)
        self.player.ammo-=1
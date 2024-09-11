from http.client import TEMPORARY_REDIRECT
from turtle import width
from entity import Entity
import pygame
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60

class Enemy(Entity,pygame.sprite.Sprite):
    def __init__(self,x,y,z,speed,hp,player,all_sprite):
        Entity.__init__(self, z,speed,hp)
        pygame.sprite.Sprite.__init__(self)

        self.animated_list.append(self.adding_animation(17,"Idle"))
        self.animated_list.append(self.adding_animation(17,"Run"))
        self.animated_list.append(self.adding_animation(9,"Attack"))

        self.image = self.animated_list[self.index_anim][self.index_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.player = player
        self.attacking = 0
        self.power = 12
        self.all_sprite = all_sprite
    

    def update(self,screen):
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)                 # hitbox


        if not self.attacking:
            dx=0
            dy=0
            # Wektor kierunku miêdzy zombie a graczem
            dx = self.player.rect.centerx - self.rect.centerx
            dy = self.player.rect.centery - self.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance != 0:
                dx /= distance
                dy /= distance
   
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if dx<0:
                self.direction = 1
            if dx>0:
                self.direction = 0
            if dx == 0 and dy == 0:
                self.index_anim = 0
            else:
                self.index_anim = 1

            #if self.rect.x < self.player.rect.x:
                #self.kill()

            if self.rect.colliderect(self.player.rect):
                self.attacking = 1
                self.index_frame = 0
        else:
            self.index_anim = 2
        self.up_animation()

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image,self.direction,False),(self.rect.x - self.player.offset_x, self.rect.y - self.player.offset_y))

    def adding_animation(self,size,nazwa_folderu):
        temp_list =[]
        for i in range(size):
            img = pygame.image.load(f'enemy/{nazwa_folderu}/{i}.png')
            img = pygame.transform.scale(img,(int(img.get_width()*self.scale),int(img.get_height()*self.scale)))
            temp_list.append(img)
        return temp_list

    def up_animation(self):
        cooldown = 100
        if pygame.time.get_ticks() - self.current_time > cooldown:
            self.current_time = pygame.time.get_ticks()
            self.index_frame += 1
            
        if len(self.animated_list[self.index_anim]) <= self.index_frame:
            self.index_frame = 0
            if self.attacking:
                self.attacking = 0
                self.index_anim = 0
                self.player.delhp(self.power)
        self.image = self.animated_list[self.index_anim][self.index_frame]



    def delhp(self,dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
            self.player.points += 5
            self.player.coins += 10

    

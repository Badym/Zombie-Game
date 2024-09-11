from http.client import TEMPORARY_REDIRECT
from entity import Entity
import pygame
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400


class Runner(Entity,pygame.sprite.Sprite):
    def __init__(self,x,y,z,speed,hp,player,all_sprite):
        Entity.__init__(self, z,speed,hp)
        pygame.sprite.Sprite.__init__(self)

        self.animated_list.append(self.adding_animation(32,"walk"))
        self.animated_list.append(self.adding_animation(32,"run"))
        self.animated_list.append(self.adding_animation(20,"attack"))
        #self.animated_list.append(self.adding_animation(9,"Attack"))
        self.run_speed = self.speed * 5
        self.image = self.animated_list[self.index_anim][self.index_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #self.rect.center = (x-30,y-30)
        self.player = player
        self.attacking = 0
        self.power = 10
        self.run = 0
        self.all_sprite = all_sprite
    

    def update(self,screen):
        if not self.attacking:
            dx=1
            dy=1

            if self.run != 1:

                # Wektor kierunku miêdzy zombie a graczem
       

                if abs(self.player.rect.centerx - self.rect.centerx) > abs(self.player.rect.centery - self.rect.centery):
                    dx = 0
                    if self.player.rect.centery - self.rect.centery > 0:
                        dy = 1
                        self.direction = 3
                    else:
                        dy = -1
                        self.direction = 2

                else:
                    if self.player.rect.centerx - self.rect.centerx > 0:
                        dx = 1
                        self.direction = 0
                    else:
                        dx = -1
                        self.direction = 1
                    dy = 0
        
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
        
  
                if self.player.rect.centerx == self.rect.centerx or self.player.rect.centery == self.rect.centery:
                    self.run = 1
                    self.index_anim = 1
                    self.index_frame = 0
                    if  self.player.rect.centerx == self.rect.centerx:
                        if self.player.rect.centery > self.rect.centery:
                            self.direction = 3
                        else:
                            self.direction = 2
                    else:
                        if self.player.rect.centerx > self.rect.centerx:
                            self.direction = 0
                        else:
                            self.direction = 1


            if self.run == 1:

                dx = 0
                dy = 0
                if self.direction == 0:
                    dx = dx + self.run_speed
                if self.direction == 1:
                    dx = dx - self.run_speed 
                if self.direction == 2:
                    dy = dy - self.run_speed
                if self.direction == 3:
                    dy = dy + self.run_speed 

            

                self.rect.x += dx 
                self.rect.y += dy 
            
        
            if self.rect.colliderect(self.player.rect):
                    self.attacking = 1
                    self.index_frame = 0



            if self.direction == 1:
                self.rotation = 180
            elif self.direction == 0:
                self.rotation = 0
            elif self.direction == 2:
                self.rotation = 90
            elif self.direction == 3: 
                self.rotation = 270
        
        else:
            self.index_anim = 2

        self.up_animation()
        self.rect.x = max(0, min(world_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(world_height - self.rect.height, self.rect.y))

        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)                 # hitbox

        #if dx<0:
        #    self.direction = 1
        #if dx>0:
        #    self.direction = 0
        #if dx == 0 and dy == 0:
        #    self.index_anim = 0
        #else:
        #    self.index_anim = 1
        
        #if self.rect.x < self.player.rect.x:
            #self.kill()


        #if self.rect.colliderect(self.player.rect):
        #    self.attacking = 1
        #    self.index_frame = 0


        
    
    def draw(self, screen):
        screen.blit(pygame.transform.rotate(self.image, self.rotation),(self.rect.x - self.player.offset_x, self.rect.y - self.player.offset_y))


    def adding_animation(self,size,nazwa_folderu):
        temp_list =[]
        for i in range(size):
            img = pygame.image.load(f'Runner/{nazwa_folderu}/{i}.png')
            img = pygame.transform.scale(img,(int((img.get_width())*self.scale),int((img.get_height())*self.scale)))
            temp_list.append(img)
        return temp_list

    def up_animation(self):
        

        cooldown = 50
        if pygame.time.get_ticks() - self.current_time > cooldown:
            self.current_time = pygame.time.get_ticks()
            self.index_frame += 1
            
        if len(self.animated_list[self.index_anim]) <= self.index_frame:
            self.index_frame = 0
            self.index_anim = 0
            self.run = 0
            if self.attacking:
                self.attacking = 0
                self.index_anim = 0
                self.player.delhp(self.power)
        self.image = self.animated_list[self.index_anim][self.index_frame]



    def delhp(self,dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
            self.player.points += 8
            self.player.coins += 12

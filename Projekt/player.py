from http.client import TEMPORARY_REDIRECT
from entity import Entity
from Pistol import Pistol
from Rifle import Rifle
from shotgun import Shotgun
import pygame
from pygame.sprite import Sprite, Group

import sys
pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 800, 600
FPS=60
healthbar_width = 200
healthbar_height = 20
healthbar_position = (10, 10)
font = pygame.font.Font('freesansbold.ttf', 20)
world_width, world_height = 3200, 2400

def draw_healthbar(surface, health, max_health):
    # Oblicz proporcje zdrowia
    health_ratio = health / max_health

    # T³o healthbara (czerwone)
    pygame.draw.rect(surface, RED, (*healthbar_position, healthbar_width, healthbar_height))
    
    # Aktualny poziom zdrowia (zielony)
    pygame.draw.rect(surface, GREEN, (*healthbar_position, healthbar_width * health_ratio, healthbar_height))

def draw_ammo_coins_counter(surface, ammo, coins):
    ammo_text = font.render(f'Ammo: {ammo}', True, BLACK)
    surface.blit(ammo_text, (healthbar_position[0], healthbar_position[1] + healthbar_height + 10))

    coin_text = font.render(f'Coins: {coins}', True, BLACK)
    surface.blit(coin_text, (healthbar_position[0], healthbar_position[1] + healthbar_height + 30))

def draw_points(surface,points):
    ammo_text = font.render(f'Points: {points}', True, BLACK)
    surface.blit(ammo_text, (350,570))

class Player(Entity,Sprite):
    def __init__(self,x,y,z,speed,hp,name):

        Entity.__init__(self, z,speed,hp)
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.animated_list.append(self.adding_animation(19,"Idle"))
        self.animated_list.append(self.adding_animation(19,"Idle_rifle"))
        self.animated_list.append(self.adding_animation(19,"Idle_shotgun"))
        self.animated_list.append(self.adding_animation(19,"Run"))
        self.animated_list.append(self.adding_animation(19,"Move_rifle"))
        self.animated_list.append(self.adding_animation(19,"Move_shotgun"))
        self.image = self.animated_list[self.index_anim][self.index_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed
        self.shoot = 0
        self.shoot_cooldown = 20
        self.shoot_col = 20
        self.cooldown_start = False
        self.start_ammo = 20
        self.ammo = self.start_ammo
        self.offset_x = 0
        self.offset_y = 0
        self.points = 0
        self.power = 15
        self.dmg = 15
        self.coins = 0
        self.nr_weapon = 0
        self.weapons = [None,None,None]
        self.weapons[0] = Pistol(self)
        self.weapons[1] = Rifle(self)
        self.weapons[2] = Shotgun(self)

        self.bullets = Group()

    def adding_animation(self,size,nazwa_folderu):
        temp_list =[]
        for i in range(size):
            img = pygame.image.load(f'player/{nazwa_folderu}/{i}.png')
            img = pygame.transform.scale(img,(int(img.get_width()*self.scale),int(img.get_height()*self.scale)))
            temp_list.append(img)
        return temp_list


    def up_animation(self):
        cooldown = 30
        if pygame.time.get_ticks() - self.current_time > cooldown:
            self.current_time = pygame.time.get_ticks()
            self.index_frame += 1
            
        if len(self.animated_list[self.index_anim]) <= self.index_frame:
            self.index_frame = 0
        self.image = self.animated_list[self.index_anim][self.index_frame]


    def update(self,screen):
        dx=0
        dy=0
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)                 # hitbox
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            dx -= self.speed
            self.direction = 1
            self.index_anim = self.nr_weapon + 3
        if keys[pygame.K_d]:
            dx += self.speed
            self.direction = 0
            self.index_anim = self.nr_weapon + 3
        if keys[pygame.K_w]:
            dy -= self.speed
            self.direction = 2
            self.index_anim = self.nr_weapon + 3
        if keys[pygame.K_s]:
            dy += self.speed
            self.direction = 3
            self.index_anim = self.nr_weapon + 3
        if keys[pygame.K_SPACE]:
            self.shoot = 1
            self.cooldown_start = True
        else:
            self.shoot = 0
        #mouse_pressed = pygame.mouse.get_pressed()
        #if mouse_pressed[0]:
        #    self.shoot = 1
        #else:
        #    self.shoot = 0
        #print(self.shoot)sa
        self.rect.x += dx
        self.rect.y += dy

        if dx == 0 and dy == 0:
            self.index_anim = self.nr_weapon

        if self.direction == 1:
            self.rotation = 180
        elif self.direction == 0:
            self.rotation = 0
        elif self.direction == 2:
            self.rotation = 90
        elif self.direction == 3: 
            self.rotation = 270

        if self.shoot and self.shoot_col == self.shoot_cooldown and self.ammo:
            self.weapons[self.nr_weapon].shoot()
        
        
        #self.bullets.update()
        #self.bullets.draw(screen)
        #print(len(self.bullets))

        self.up_animation()
        if self.cooldown_start:
            self.shoot_col-=1
        if not self.shoot_col:
            self.cooldown_start = False
            self.shoot_col = self.shoot_cooldown

        # Obliczanie przesuniêcia kamery
        self.offset_x = self.rect.x - WIDTH // 2 + self.rect.width // 2
        self.offset_y = self.rect.y - HEIGHT // 2 + self.rect.height // 2

        

        # Ograniczenie przesuniêcia kamery do granic œwiata
        self.offset_x = max(0, min(self.offset_x, world_width - WIDTH))
        self.offset_y = max(0, min(self.offset_y, world_height - HEIGHT))


    def draw(self, screen): 
        screen.blit(pygame.transform.rotate(self.image, self.rotation), (self.rect.x - self.offset_x, self.rect.y - self.offset_y))
        draw_healthbar(screen,self.hp,self.max_hp)
        draw_ammo_coins_counter(screen,self.ammo,self.coins)
        draw_points(screen,self.points)

    def delhp(self,dmg):
        self.hp -= dmg
        print("zycie: ",self.hp)
        if self.hp <= 0:
            self.kill()

    def change_weapon(self,nr):
        self.nr_weapon = nr
        self.weapons[self.nr_weapon].set()



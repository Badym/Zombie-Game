from http.client import TEMPORARY_REDIRECT
import pygame



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,speed,num_img,direction,home):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.scale = scale
        self.image = pygame.image.load(f'bullets/{num_img}.png')
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width()*self.scale),int(self.image.get_height()*self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.home = home
        self.endlife = 0
        

    def update(self,gh):
        dx,dy = 0,0
        if self.direction == 0:
            dx += self.speed
        if self.direction == 1:
            dx -= self.speed
        if self.direction == 2:
            dy -= self.speed
        if self.direction == 3:
            dy += self.speed

        self.rect.x += dx
        self.rect.y += dy

        if self.direction == 1:
            self.rotation = 90
        elif self.direction == 0:
            self.rotation = 270
        elif self.direction == 2:
            self.rotation = 0
        elif self.direction == 3:
            self.rotation = 180


        if self.rect.right < 0 or self.rect.left > world_width or self.rect.bottom > world_height or self.rect.bottom < 0:
            self.kill()

        
        for asd in gh.entities:
            if asd != self.home:
                if pygame.sprite.spritecollide(asd,self.home.bullets,False):
                    self.kill()
                    asd.delhp(self.home.dmg)
                    


    def draw(self,screen):
        screen.blit(pygame.transform.rotate(self.image, self.rotation),(self.rect.x - self.home.offset_x, self.rect.y - self.home.offset_y))



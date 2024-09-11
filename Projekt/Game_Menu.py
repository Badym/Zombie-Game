import pygame
from Button import Button
from map import Game_Map
from TextBox import TextBox
from Ranking import Ranking
import sys



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RCOLOR = (34,135,12)
WIDTH, HEIGHT = 800, 600
FPS=60
world_width, world_height = 3200, 2400

class Game_Menu:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Horda")

        self.screen = screen

        ammo_img = pygame.image.load("ammo.png")
        self.ammo_button = Button(720,15,ammo_img,4)

        pistol_img = pygame.image.load("Buttons\pistol.png")
        self.pistol_button = Button(720,55,pistol_img,0.4)

        rifle_img = pygame.image.load("rifle.png")
        self.rifle_button = Button(720,105,rifle_img,0.4)

        shotgun_img = pygame.image.load("Buttons\shotgun.png")
        self.shotgun_button = Button(720,155,shotgun_img,0.4)

        play_img = pygame.image.load("Buttons\play.png")
        self.play_button = Button(300,125,play_img,1)

        score_img = pygame.image.load("Buttons\score.png")
        self.score_button = Button(300,225,score_img,1)
        self.first = 0
        quit_img = pygame.image.load("Buttons\quit.png")
        self.quit_button = Button(300,325,quit_img,1)
        self.input_box = TextBox(100, 100, 140, 32)
        self.game_paused = True
        ranking = Ranking("players.txt")
        self.slide = [ranking, None]
        self.slide[0] = ranking
        self.num = 0

    def update(self):

        running = True
        clock = pygame.time.Clock()


        while running:
            self.screen.fill((100, 50, 70))
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.input_box.handle_event(event)
            
            self.input_box.draw(self.screen)
       
            if self.game_paused:
                
                if self.play_button.draw(self.screen) and len(self.input_box.text):
                    self.slide[1] = Game_Map(self.input_box.text)
                    self.game_paused = False
                    self.num = 1
                elif self.score_button.draw(self.screen):
                    self.num = 0
                    self.game_paused = False
                    print(self.input_box.text)
                elif self.quit_button.draw(self.screen):
                    running = False
            else:

                self.game_paused = self.slide[self.num].update(self.screen)
                if not self.game_paused and self.num == 1:
                    if self.ammo_button.draw(self.screen):
                        if self.slide[1].player.coins >= 15:
                            self.slide[1].player.ammo += 20
                            self.slide[1].player.coins -= 15
                    elif self.pistol_button.draw(self.screen):
                        self.slide[1].player.nr_weapon = 0
                        self.slide[1].player.weapons[0].set()
                    elif self.rifle_button.draw(self.screen):
                        self.slide[1].player.nr_weapon = 1
                        self.slide[1].player.weapons[1].set()
                    elif self.shotgun_button.draw(self.screen):
                        self.slide[1].player.nr_weapon = 2
                        self.slide[1].player.weapons[2].set()

                if self.num == 1 and self.game_paused:
                    self.slide[0].add_record(self.slide[1].player.name,self.slide[1].player.points)
                    #self.slide[0].add_record("asas",23232323)
                    self.game_paused = True
                    self.slide[1] = Game_Map(self.input_box.text)
                

            pygame.display.flip()
        pygame.quit()












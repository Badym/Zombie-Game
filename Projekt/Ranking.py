from turtle import screensize
import pygame
import sys
import itertools
from Button import Button
import re
from pathlib import Path

class Ranking:
    def __init__(self, file_path):
        self.file_path = file_path
        self.players = self.load_ranking()
        self.x = 0

        right_img = pygame.image.load("right.png")
        self.right_button = Button(700,550,right_img,1)

        left_img = pygame.image.load("Buttons\left.png")
        self.left_button = Button(650,550,left_img,1)

        x_img = pygame.image.load("x.png")
        self.x_button = Button(750,550,x_img,1)

    def load_ranking(self):
        file_path = Path(self.file_path)
        players = []
        if file_path.exists():
            with file_path.open('r') as file:
                for line in file:
                    line = line.strip()
                    match = re.match(r'([^;]+);(\d+)', line)
                    if match:
                        name, score = match.groups()
                        print(f'Name: {name}, Score: {score}')
                        players.append((name, int(score)))
                players.sort(key=lambda x: x[1], reverse=True)  # Sortowanie malej¹co wed³ug punktów
        else:
            print(f'Plik {file_path} nie istnieje.')
        return players

        
    #def load_ranking(self):
    #    players = []
    #    with open(self.file_path, 'r', encoding='latin-1') as file:
    #        for line in file:
    #            name, score = line.strip().split(";")
    #            players.append((name, int(score)))
    #    players.sort(key=lambda x: x[1], reverse=True)  # Sortowanie malej¹co wed³ug punktów
    #    return players
    
    def update(self,screen):
        
        font = pygame.font.SysFont(None, 30)
       
            
        screen.fill((0, 0, 0))
        x_offset = 0   
        y_offset = 50
        n = self.x
        for name, score in itertools.islice(self.players, self.x, None):
            n+=1
            text = font.render(f"{n}. {name}: {score}", True, (255, 255, 255))
            screen.blit(text, (50 + x_offset, y_offset))
            y_offset += 50
            if n == self.x + 9:
                x_offset += 320
                y_offset = 50
            if n == self.x + 18:
                break
        if self.x_button.draw(screen):
            return True
        if self.right_button.draw(screen):
            if len(self.players) > self.x: 
                self.x += 18
        if self.left_button.draw(screen):
            if self.x >= 18:
                self.x -= 18
        return False

    def save_data(self):
        with open(self.file_path, 'w') as file:
            for player in self.players:
                name, score = player
                file.write(f"{name};{score}\n")

    def add_record(self,name,score):
        self.players.append((name,int(score)))
        
        self.players.sort(key=lambda x: x[1], reverse=True)  # Sortowanie malej¹co wed³ug punktów
        for i in self.players:
            print(i[0],i[1])
        self.save_data()

    



                



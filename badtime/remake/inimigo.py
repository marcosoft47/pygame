import pygame
from pygame.locals import *
import random

enemy_size = 30
enemy_speed = 5

largura = 1920
altura = 1020
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
class Inimigo():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xdir = 1
        self.ydir = 1
        self.sprites = []
        self.atual = 0
        self.type = random.randint(0,2)
        if self.type == 0:
            if random.randint(0,1) == 0:
                self.x = largura
                self.xdir = -1
            if random.randint(0,1) == 0:
                self.y = altura
                self.ydir = -1
        elif self.type == 1:
            self.y = random.randint(0,altura-enemy_size)
            self.ydir = 0
            if random.randint(0,1) == 0:
                self.xdir = -1
        elif self.type == 2:
            self.x = random.randint(0,largura-enemy_size)
            self.xdir = 0
            if random.randint(0,1) == 0:
                self.ydir = -1
        self.ret = pygame.draw.rect(tela, (255,255,0), (self.x,self.y,enemy_size,enemy_size))
    def update(self):
        self.x += enemy_speed * self.xdir * 0.75
        self.y += enemy_speed * self.ydir * 0.75
        if self.x >= largura + enemy_size:
            self.x = -enemy_size
        if self.x <= -enemy_size-1:
            self.x = largura+enemy_size-1
        if self.y >= altura + enemy_size:
            self.y = -enemy_size
        if self.y <= -enemy_size-1:
            self.y = altura-1
    def render(self):
        self.ret = pygame.draw.rect(tela, (255,255,0), (self.x,self.y,enemy_size,enemy_size))

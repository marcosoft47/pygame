import pygame
from pygame.locals import *
import random
import sys
import math
class Inimigo():
    def __init__(self):
        global largura,altura,size,tela
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
            self.y = random.randint(0,altura-40)
            self.ydir = 0
            if random.randint(0,1) == 0:
                self.xdir = -1
        elif self.type == 2:
            self.x = random.randint(0,largura-40)
            self.xdir = 0
            if random.randint(0,1) == 0:
                self.ydir = -1
        self.ret = pygame.draw.rect(tela, (255,255,0), (self.x,self.y,size,size))
    def update(self):
        global largura,altura,size
        self.x += espeed * self.xdir * 0.75
        self.y += espeed * self.ydir * 0.75
        if self.x >= largura + size:
            self.x = -size
        if self.x <= -size-1:
            self.x = largura+size-1
        if self.y >= altura + size:
            self.y = -size
        if self.y <= -size-1:
            self.y = altura-1
    def render(self):
        self.ret = pygame.draw.rect(tela, (255,255,0), (self.x,self.y,size,size))
pygame.init()
pygame.font.init()
largura = 1920
altura = 1020
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption('ricardofm.me')

speed = 10
espeed = 5
size = 30
x = largura//2
y = altura//2
x_maca = random.randint(0, largura)
y_maca = random.randint(0, altura)
snake = pygame.draw.rect(tela, (128,0,255), (x,y,size,size))
maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size,size))
fundo = (0,0,0)

enemy = []

fonte = pygame.font.SysFont('aakar', 40, True, True)
pontos = 0
gameover= fonte.render('Melhore Aperte R para recomecar', True, (255,255,255))
recomecar = True

musica = pygame.mixer.music.load('sans_undertale.ogg')
pygame.mixer.music.play(-1)
rapaz = pygame.mixer.Sound('rapaz.ogg')
som = pygame.mixer.Sound('snd_hurt1.wav')
gitgud = pygame.mixer.Sound('mus_f_laugh.wav')
contar = 0



relogio = pygame.time.Clock()
running = True
while running:
    relogio.tick(60)
    tela.fill(fundo)
    largura, altura = tela.get_size()
    mensagem = f'Pontos: {pontos}'
    pontuacao = fonte.render(mensagem, True, (255,255,255))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == KEYDOWN:
            if e.key == K_r:
                recomecar = True
                enemy.clear()
                pontos = 0
                pygame.mixer.music.play(-1)
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    if recomecar:
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            x -= speed
        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            x += speed
        if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
            y -= speed
        if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
            y += speed
        
        if x >= largura + size:
            x = -size
        if x <= -size-1:
            x = largura+size-1
        if y >= altura + size:
            y = -size
        if y <= -size-1:
            y = altura-1
        
        if snake.colliderect(maca):
            pontos += 5
            x_maca = random.randint(0, largura-size)
            y_maca = random.randint(0, altura+size)
            som.play()
            if pontos % 5 == 0:
                enemy.append(Inimigo())
            if pontos == 69:
                rapaz.play()
        for i in range(len(enemy)):
            if snake.colliderect(enemy[i].ret):
                gitgud.play()
                recomecar = False
                pygame.mixer.music.stop()
            enemy[i].update()
    else:
        tela.blit(gameover, (largura//3,altura//2))
    snake = pygame.draw.rect(tela, (128,0,255), (x,y,size*0.5,size*0.5))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size*1.5,size*1.5))

    for i in range(len(enemy)):
        enemy[i].render()
    tela.blit(pontuacao, (largura-(largura/3), 30))
    pygame.display.flip()
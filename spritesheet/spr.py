import pygame
from pygame.locals import *
from sys import exit
import os
import random

pygame.init()
pygame.mixer.init()

pwd = os.path.dirname(__file__)
path_imagens = os.path.join(pwd, 'imagens')
path_sons = os.path.join(pwd, 'sons')

largura = 1280
altura = 640
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Guy')
AZULCLARO = (192,255,255)
BRANCO = (255,255,255)

speed = 5
bateu = False
escolha_obstaculo = random.choice([0,1])

spr_kid = pygame.image.load(os.path.join(path_imagens, 'kid.png')).convert_alpha()
spr_fruit = pygame.image.load(os.path.join(path_imagens, 'fruit.png')).convert_alpha()
spr_spike = pygame.image.load(os.path.join(path_imagens, 'spike.png')).convert_alpha()
spr_block = pygame.image.load(os.path.join(path_imagens, 'block.png')).convert_alpha()
spr_cloud = pygame.image.load(os.path.join(path_imagens, 'cloud.png')).convert_alpha()

snd_pulo = pygame.mixer.Sound(os.path.join(path_sons, 'teleport_in.wav'))
snd_gameover = pygame.mixer.Sound(os.path.join(path_sons, 'gameover.ogg'))
pygame.mixer.music.load(os.path.join(path_sons, 'moon.ogg'))
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

class Kid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = snd_pulo
        self.som_pulo.set_volume(.5)
        self.frames_kid = []
        for i in range(6):
            img  = spr_kid.subsurface((32*i,0),(32,32))
            img = pygame.transform.scale(img, (32*4, 32*4))
            self.frames_kid.append(img)
        self.index_frames = 0
        self.image = self.frames_kid[self.index_frames]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = altura - 64*3
        self.rect.center = (largura//3, self.pos_y_inicial)
        self.pulo = False

    def update(self):
        if self.pulo:
            if self.rect.y <= altura//4:
                self.pulo = False
            self.rect.y -= speed*2
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += speed*2
            else:
                self.rect.y = self.pos_y_inicial
        if self.index_frames > 5:
            self.index_frames = 0
        self.index_frames += 0.25
        self.image = self.frames_kid[int(self.index_frames)]

    def pular(self):
        self.pulo = True
        self.som_pulo.play()


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr_cloud
        self.image = pygame.transform.scale(self.image, (32*3,32*3))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(50,300,25)
        self.rect.x = random.randint(0,largura)
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = random.randrange(50,300, 25)
        self.rect.x -= speed

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr_block
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 64
        self.rect.x = 64*pos
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 5

class Espinho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr_spike
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottomleft = (largura, altura-64)
        self.rect.x = largura

        self.escolha = escolha_obstaculo
    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= 5

class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spr_fruit
        self.image = pygame.transform.scale(self.image, (32*2,32*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (largura, 300)
        self.rect.x = largura

        self.escolha = escolha_obstaculo
    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= 5


allsprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

for i in range(20):
    nuvem = Nuvens()
    allsprites.add(nuvem)

for i in range(largura*10//64):
    chao = Chao(i)
    allsprites.add(chao)

espinho = Espinho()
allsprites.add(espinho)

obstaculos.add(espinho)

fruta = Fruta()
allsprites.add(fruta)
obstaculos.add(fruta)

kid = Kid()
allsprites.add(kid)


relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    tela.fill(AZULCLARO)
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if kid.rect.y == kid.pos_y_inicial:
                    kid.pular()
    
    if espinho.rect.topright[0] <= 0 or fruta.rect.topright[0] <= 0:
        escolha_obstaculo = random.choice([0,1])
        espinho.rect.x = largura
        fruta.rect.x = largura
        espinho.escolha = escolha_obstaculo
        fruta.escolha = escolha_obstaculo

    colisoes = pygame.sprite.spritecollide(kid, obstaculos, False, pygame.sprite.collide_mask)

    allsprites.draw(tela)
    if colisoes and not bateu:
        bateu = True
        pygame.mixer.music.stop()
        snd_gameover.play()
    if bateu:
        pass
    else:
        allsprites.update()

    pygame.display.flip()
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

class Dog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("sprites/dog_1.png"))
        self.sprites.append(pygame.image.load("sprites/dog_2.png"))
        self.sprites.append(pygame.image.load("sprites/dog_3.png"))
        self.sprites.append(pygame.image.load("sprites/dog_4.png"))
        self.sprites.append(pygame.image.load("sprites/dog_5.png"))
        self.sprites.append(pygame.image.load("sprites/dog_6.png"))
        self.sprites.append(pygame.image.load("sprites/dog_7.png"))
        self.sprites.append(pygame.image.load("sprites/dog_8.png"))
        self.sprites.append(pygame.image.load("sprites/dog_9.png"))
        self.sprites.append(pygame.image.load("sprites/dog_10.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (21*10, 83*10))
        self.rect = self.image.get_rect()
        self.rect.center = largura//2, 0

    def update(self):
    
        self.atual += 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (21*10, 83*10))


largura = 1920
altura = 1020
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPRITE!")

allSprites = pygame.sprite.Group()
dog = Dog()
allSprites.add(dog)

fundo = pygame.image.load("sprites/Lake_Tess.png").convert()
fundo = pygame.transform.scale(fundo, (largura, altura))

relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(fundo, (0,0))
    allSprites.draw(tela)
    allSprites.update()
    pygame.display.flip()

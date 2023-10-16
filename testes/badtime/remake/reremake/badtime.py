import pygame
from pygame.locals import *
from sys import exit
pygame.init()

# Setup
largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))
tela.fill((255,255,255))

x = 0
y = altura//2
tamanho = 50
retangulo = pygame.draw.rect(tela, (128,0,255), (x,y,tamanho,tamanho))

relogio = pygame.time.Clock()
while True:
    relogio.tick(60)

    #Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
        if e.type == KEYDOWN:
            pass

    if pygame.key.get_pressed()[K_UP]:
        y -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        y += 5
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    #Update
    if x > largura:
        x = -tamanho
    if x < -tamanho - 1:
        x = largura
    if y > altura:
        y = -tamanho
    if y < -tamanho - 1:
        y = altura
    #Renderizar
    tela.fill((255,255,255))
    retangulo = pygame.draw.rect(tela, (128,0,255), (x,y,tamanho,tamanho))
    pygame.display.flip()
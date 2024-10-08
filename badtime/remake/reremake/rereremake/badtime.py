import pygame
from pygame.locals import *
from sys import exit
pygame.init()
#setup
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("Colmeia")


largura_jogador = 100
altura_jogador = largura_jogador
x_jogador = largura_tela//2
y_jogador = altura_tela//2
jogador = pygame.draw.rect(tela, (128,0,255), (x_jogador,y_jogador,largura_jogador,altura_jogador))

relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    #eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
    
    if pygame.key.get_pressed()[K_UP]:
        y_jogador -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        y_jogador += 5
    if pygame.key.get_pressed()[K_LEFT]:
        x_jogador -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x_jogador += 5

    #update

    if x_jogador > largura_tela:
        x_jogador = -largura_jogador
    if x_jogador < -largura_jogador:
        x_jogador = largura_tela
    if y_jogador > altura_tela:
        y_jogador = -altura_jogador
    if y_jogador < -altura_jogador:
        y_jogador = altura_tela
    #render
    tela.fill((255,255,255))
    jogador = pygame.draw.rect(tela, (128,0,255), (x_jogador,y_jogador,largura_jogador,altura_jogador))
    pygame.display.flip()
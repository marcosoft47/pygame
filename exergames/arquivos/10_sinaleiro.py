import pygame
import time

pygame.init()
largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')

figura_1=pygame.image.load('figura_1_vermelho.png')
figura_2=pygame.image.load('figura_2_amarelo.png')
figura_3=pygame.image.load('figura_3_verde.png')

run = True

while run: 

    tela.blit(figura_3, (0, 0))
    pygame.display.update()
    time. sleep(1)

    tela.blit(figura_2, (0, 0))
    pygame.display.update()
    time. sleep(1)

    tela.blit(figura_1, (0, 0))
    pygame.display.update()
    time. sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False       
     
pygame.quit()

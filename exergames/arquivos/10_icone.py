import pygame
import time

pygame.init()
largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')

icon=pygame.image.load('figura_3_verde.png')
pygame.display.set_icon(icon)
run = True

while run: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False       
     
pygame.quit()

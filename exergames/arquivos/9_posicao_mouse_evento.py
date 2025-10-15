import pygame
import pygame.display
import pygame.event

pygame.init()

largura_tela = 640
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicou!")
            print(event)

        if event.type == pygame.MOUSEBUTTONUP:
            print("Soltou!")
            print(event)
     
pygame.quit()
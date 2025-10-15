import pygame

pygame.init()
largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')
run = True

while run: 

    pygame.draw.rect(tela, "yellow", [0,0,630,240])
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False       
     
pygame.quit()

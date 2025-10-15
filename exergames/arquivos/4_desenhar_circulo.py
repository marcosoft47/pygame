import pygame

pygame.init()
largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')
run = True

while run: 

    pygame.draw.circle(tela, "white", ((largura_tela/2),(altura_tela/2)), 50)
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False       
     
pygame.quit()
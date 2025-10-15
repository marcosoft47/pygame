import pygame

pygame.init()

largura_tela = 640
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
run = True

while run:

    pos = pygame.mouse.get_pos()
    print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
     
pygame.quit()
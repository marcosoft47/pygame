import pygame

pygame.init()
largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')

fonte = pygame.font.SysFont("Arial",40, bold=True, italic=True)
run = True

while run: 

    texto = fonte.render('MEU PYANO', True, 'white')
    tela.blit(texto, [(180), (60)])
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False       
     
pygame.quit()
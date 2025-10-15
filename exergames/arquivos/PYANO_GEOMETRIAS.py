import pygame
import pygame.display

pygame.init()

largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')


inicio_y_teclas = 240
largura_tecla = 90
altura_tecla = 280

inicio_x_do = 0
inicio_x_re = 90
inicio_x_mi = 180
inicio_x_fa = 270
inicio_x_sol = 360
inicio_x_la = 450
inicio_x_si = 540

fonte = pygame.font.SysFont("Arial",40, bold=True, italic=True)


run = True

while run:

    pos = pygame.mouse.get_pos()
    print(pos)

    pygame.draw.rect(tela, "black", [0,0,largura_tela,240])
    pygame.draw.line(tela, "white", (0,240), (640,240), 50)

    pygame.draw.rect(tela, "red", [inicio_x_do,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "orange", [inicio_x_re,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "yellow", [inicio_x_mi,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "green", [inicio_x_fa,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "pink", [inicio_x_sol,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "purple", [inicio_x_la,inicio_y_teclas,largura_tecla,altura_tecla])
    pygame.draw.rect(tela, "blue", [inicio_x_si,inicio_y_teclas,largura_tecla,altura_tecla])
    

    pygame.draw.circle(tela, "white", (pos), 5)
    pygame.draw.circle(tela, "black", (pos), 3)

    pygame.draw.ellipse(tela, "yellow", (80,35,440,100),5)

    texto = fonte.render('MEU PYANO', True, 'white')
    tela.blit(texto, [(180), (60)])
    texto_do = fonte.render('DÓ', True, 'white')
    tela.blit(texto_do, [(10), (400)])
    texto_re = fonte.render('RÉ', True, 'white')
    tela.blit(texto_re, [(105), (400)])
    texto_mi = fonte.render('MI', True, 'white')
    tela.blit(texto_mi, [(200), (400)])
    texto_fa = fonte.render('FÁ', True, 'white')
    tela.blit(texto_fa, [(290), (400)])
    texto_sol = fonte.render('SOL', True, 'white')
    tela.blit(texto_sol, [(360), (400)])
    texto_la = fonte.render('LÁ', True, 'white')
    tela.blit(texto_la, [(470), (400)])
    texto_si = fonte.render('SI', True, 'white')
    tela.blit(texto_si, [(560), (400)])


    pygame.display.flip()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
     
pygame.quit()
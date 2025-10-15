import pygame
import cv2
import numpy as np

pygame.init()

largura = 480
altura = 270
tela= pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Imagem Original')
vertices = np.zeros((4, 2), int)
contador = 0

imagem_pygame=pygame.image.load('perspectiva_1.jpeg')
imagem_original = cv2.imread('perspectiva_1.jpeg')
run = True

def background (imagem_pygame):
    tela.blit(imagem_pygame, (0, 0))


while run:      
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if contador<4:
                pos = pygame.mouse.get_pos()
                vertices[contador] = pos
                contador=contador+1

       
    background (imagem_pygame)

    if contador>0:
        pygame.draw.circle(tela, (255,0,0), (vertices[0]), 5)
    if contador>1:
        pygame.draw.circle(tela, (255,0,0), (vertices[0]), 5)
        pygame.draw.circle(tela, (0,255,0), (vertices[1]), 5)
    if contador>2:
        pygame.draw.circle(tela, (255,0,0), (vertices[0]), 5)
        pygame.draw.circle(tela, (0,255,0), (vertices[1]), 5)
        pygame.draw.circle(tela, (0,255,255), (vertices[2]), 5)
    if contador>3:
        pygame.draw.circle(tela, (255,0,0), (vertices[0]), 5)
        pygame.draw.circle(tela, (0,255,0), (vertices[1]), 5)
        pygame.draw.circle(tela, (0,255,255), (vertices[2]), 5)
        pygame.draw.circle(tela, (0,0,255), (vertices[3]), 5)

        pontos_1 = np.float32([[vertices[0]],[vertices[1]], [vertices[2]], [vertices[3]]])
        pontos_2 = np.float32([[0,0], [largura,0],[0,altura],[largura,altura]])
        matrix = cv2.getPerspectiveTransform(pontos_1,pontos_2)
        imagem_corrigida = cv2.warpPerspective(imagem_original,matrix,(largura,altura))
        cv2.imshow("Imagem Corrigida", imagem_corrigida)
   
    pygame.display.update()
     
pygame.quit()
import pygame
from pygame.locals import *
import random
import sys
from inimigo import Inimigo, largura, altura, tela

pygame.init()
pygame.font.init()
pygame.display.set_caption('badtime')

speed = 10
size = 30
x = largura//2
y = altura//2
snake = pygame.draw.rect(tela, (128,0,255), (x,y,size,size))

x_maca = random.randint(0, largura)
y_maca = random.randint(0, altura)
maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size,size))
fundo = (0,0,0)

enemy = []

fonte = pygame.font.SysFont('aakar', 40, True, True)
pontos = 0
gameover= fonte.render('Melhore Aperte R para recomecar', True, (255,255,255))
recomecar = True

pygame.mixer.music.load('sans_undertale.ogg')
pygame.mixer.music.play(-1)
som = pygame.mixer.Sound('snd_hurt1.wav')
gitgud = pygame.mixer.Sound('mus_f_laugh.wav')



relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    tela.fill(fundo)
    largura, altura = tela.get_size()
    mensagem = f'Pontos: {pontos}'
    pontuacao = fonte.render(mensagem, True, (255,255,255))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if e.type == KEYDOWN:
            if e.key == K_r:
                recomecar = True
                enemy.clear()
                pontos = 0
                pygame.mixer.music.play(-1)
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    if recomecar:
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            x -= speed
        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            x += speed
        if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
            y -= speed
        if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
            y += speed
        
        if x >= largura + size:
            x = -size
        if x <= -size-1:
            x = largura+size-1
        if y >= altura + size:
            y = -size
        if y <= -size-1:
            y = altura-1
        
        if snake.colliderect(maca):
            pontos += 5
            x_maca = random.randint(0, largura-size//2)
            y_maca = random.randint(0, altura-size//2)
            som.play()
            if pontos % 5 == 0:
                enemy.append(Inimigo())
        for i in range(len(enemy)):
            if snake.colliderect(enemy[i].ret):
                gitgud.play()
                recomecar = False
                pygame.mixer.music.stop()
            enemy[i].update()
    else:
        tela.blit(gameover, (largura//3,altura//2))

    snake = pygame.draw.rect(tela, (128,0,255), (x,y,size*0.5,size*0.5))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size*1.5,size*1.5))

    for i in range(len(enemy)):
        enemy[i].render()
    tela.blit(pontuacao, (largura-(largura/3), 30))
    pygame.display.flip()
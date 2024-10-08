import pygame
from pygame.locals import *
import random
import sys
import math
pygame.init()
pygame.font.init()
largura = 1080
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('snake')

def aumentacorpo(lista_cobra):
    for i in lista_cobra:
        pygame.draw.rect(tela, cor_snake, (i[0],i[1],size,size))

pos_corpo = []
speed = 7
size = 30

x = largura//3
xdir = speed
y = altura//2
ydir = 0
pos_corpo = []
comprimento = 20
x_maca = random.randint(0, largura)
y_maca = random.randint(0, altura)
cor_snake = (128,0,255)
snake = pygame.draw.rect(tela, (128,0,255), (x,y,size,size))
maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size,size))
fundo = (0,0,0)

fonte = pygame.font.SysFont('aakar', math.floor(size*1.5), True, True)
pontos = 0
gameover= fonte.render('Melhore Aperte R para recomecar', True, (255,255,255))
recomecar = True

musica = pygame.mixer.music.load('badtime/sans_undertale.ogg')
pygame.mixer.music.play(-1)
rapaz = pygame.mixer.Sound('badtime/rapaz.ogg')
som = pygame.mixer.Sound('badtime/snd_hurt1.wav')
gitgud = pygame.mixer.Sound('gameover.ogg')
contar = 0


relogio = pygame.time.Clock()
running = True
while running:
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
            if e.key == K_a and xdir == 0:
                xdir = -speed
                ydir = 0
            if e.key == K_d and xdir == 0:
                xdir = speed
                ydir = 0
            if e.key == K_w and ydir == 0:
                xdir = 0
                ydir = -speed
            if e.key == K_s and ydir == 0:
                xdir = 0
                ydir = speed
            if e.key == K_r:
                x = largura//3
                xdir = speed
                y = altura//2
                ydir = 0
                pos_corpo = []
                comprimento = 20
                x_maca = random.randint(0, largura-size)
                y_maca = random.randint(0, altura-size)

                recomecar = True
                pontos = 0
                pygame.mixer.music.play(-1)
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
    
    if recomecar:
        '''if pygame.key.get_pressed()[K_a]:
            x -= speed
        if pygame.key.get_pressed()[K_d]:
            x += speed
        if pygame.key.get_pressed()[K_w]:
            y -= speed
        if pygame.key.get_pressed()[K_s]:
            y += speed'''

        x += xdir
        y += ydir
        pos_cabeca = [x,y]
        pos_corpo.append(pos_cabeca)
        aumentacorpo(pos_corpo)

        if len(pos_corpo) > comprimento:
            del pos_corpo[0]
        if pos_corpo.count(pos_cabeca) > 1:
            gitgud.play()
            recomecar = False
            pygame.mixer.music.stop()

        if x >= largura + size:
            x = -size
        if x <= -size-1:
            x = largura+size-1
        if y >= altura + size:
            y = -size
        if y <= -size-1:
            y = altura-1
        
        if snake.colliderect(maca):
            pontos += 1
            comprimento += 5
            x_maca = random.randint(0, largura-size)
            y_maca = random.randint(0, altura-size)
            som.play()
            if pontos == 69:
                rapaz.play()
        snake = pygame.draw.rect(tela, cor_snake, (x,y,size,size))
        maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,size,size))
    else:
        ret_gameover = gameover.get_rect()
        ret_gameover.center = (largura//2,altura//2)
        tela.blit(gameover, ret_gameover)
    ret_pontos = pontuacao.get_rect()
    ret_pontos.topright = (largura-10,10)
    tela.blit(pontuacao, ret_pontos)
    pygame.display.update()
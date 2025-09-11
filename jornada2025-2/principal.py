import pygame
from pygame import display
from pygame import event
from pygame import font
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, KEYUP, K_SPACE
from pygame.time import Clock
from pygame.transform import scale
from pygame.image import load
import botao
from jogador import Jogador
from pygame.sprite import GroupSingle, Group, groupcollide
from inimigo import Inimigo

class Jogo():
    def __init__(self):
        pygame.init()
        self.running = True
        self.estado = 0
        self.tamanho = 800, 600
        self.superficie = display.set_mode(
            size = self.tamanho,
            display=0   
        )
        display.set_caption('Galaga')
        self.fonteDestaque = font.SysFont('monocraft', 80)
        self.imagemInicio = pygame.image.load('images/button_inicio.png').convert_alpha()
        self.imagemSair = pygame.image.load('images/button_sair.png').convert_alpha()

        self.botaoInicio = botao.Botao(30, 450, self.imagemInicio, 0.8)
        self.botaoSair = botao.Botao(600, 450, self.imagemSair, 0.8)

        self.clock = Clock()
        self.fundo = scale(
            load('images/space.jpg'),
            self.tamanho
        )
        self.fonte = font.SysFont('monocraft', 50)


    def novo_jogo(self):
        self.grupoInimigos = Group()
        self.grupoTiros = Group()
        self.jogador = Jogador(self)
        self.grupoJogador = GroupSingle(self.jogador) # type: ignore
        self.grupoInimigos.add(Inimigo(self))
        self.round = 0
        self.mortes = 0

    def rodar(self):
        while self.running:
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        self.running = False
                if self.estado == 1:
                    if e.type == KEYUP:
                        if e.key == K_SPACE:
                            self.jogador.atirar()

            # Menu Principal
            if self.estado == 0:
                self.superficie.fill((0,0,20))
                titulo = self.fonteDestaque.render(
                    'Galaga',
                    True,
                    (255,255,255)
                )
                self.superficie.blit(titulo,(250,180))
                if self.botaoInicio.criar(self.superficie):
                    self.estado = 1
                    self.novo_jogo()
                if self.botaoSair.criar(self.superficie):
                    self.running = False

            elif self.estado == 1:
                self.clock.tick(120)
                # Update
                self.jogador.update()

                self.round += 1
                if self.round % 120 == 0:
                    self.grupoInimigos.add(Inimigo(self))
                self.grupoInimigos.update()
                self.grupoTiros.update()
                if groupcollide(
                    self.grupoTiros,
                    self.grupoInimigos,
                    True,
                    True
                ):
                    self.mortes += 1
                fonteMortes = self.fonte.render(
                    f'Morte: {self.mortes}',
                    True,
                    (255,255,255)
                )

                # Render
                self.superficie.blit(self.fundo, (0,0))
                self.grupoJogador.draw(self.superficie)
                self.grupoInimigos.draw(self.superficie)
                self.grupoTiros.draw(self.superficie)
                self.superficie.blit(fonteMortes, (20,20))
            elif self.estado == 2:
                self.superficie.fill((255,0,0))
            # Tela de Jogo
            display.update()

g = Jogo()
g.rodar()

pygame.quit()
exit()
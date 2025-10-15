import pygame

MAX_KEYS = 7
WIDTH = 640
HEIGHT = 480

SIZE = WIDTH/MAX_KEYS

class Teclas():
    def __init__(self, pos: int, nome: str, arquivo: str, cor: tuple[int,int,int]):
        self.som = pygame.mixer.Sound(arquivo)
        self.nota = nome
        self.pos = pos
        self.cor = cor
    
    def criar(self, surface):
        action = False

        pygame.draw.rect(surface, self.cor, [WIDTH//self.pos*MAX_KEYS, HEIGHT//2,WIDTH,HEIGHT])
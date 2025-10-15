import pygame
import random
from settings import tamanho_tela

class Sequencia():
    def __init__(self, x: int, y: int, image: pygame.surface.Surface, speed: int):
        self.next = 4
        self.sortear()
        self.imageOriginal = pygame.transform.rotate(image,-45)
        self.image = pygame.transform.rotate(self.imageOriginal, 90*self.next)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = speed

    def sortear(self):
        ''' Sortea direções aleatórias'''
        self.next = random.randint(1,4)
    
    def update(self, surface:pygame.surface.Surface):
        self.rect.y += self.velocidade
        if self.rect.y == tamanho_tela[1]//2:
            self.rect.y = -200
            self.sortear()
            self.image = pygame.transform.rotate(self.imageOriginal, 90*self.next)
    

    def render(self, surface: pygame.surface.Surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
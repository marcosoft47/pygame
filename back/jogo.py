import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

import flecha
import sequencia
from settings import path_assets, tamanho_tela

class Jogo():
    def __init__(self):
        pygame.init()
        self.running = True
        self.tamanho = tamanho_tela
        self.superficie = pygame.display.set_mode(
            size = self.tamanho,
            display = 0
        )
        pygame.display.set_caption('Dança Gatinho Dança')
        self.fundo = (255,255,255) # Branco

        self.imagemFlecha = pygame.image.load(os.path.join(path_assets, 'temp_flecha.png'))

        #  N
        # O L
        #  S
        
        __N = 200
        __S = 400
        __L = 450
        __O = 150
        self.flechaNO = flecha.Flecha(
            x = __O, 
            y = __N, 
            image = pygame.transform.rotate(self.imagemFlecha,45),
            number = 1
        )
        self.flechaSO = flecha.Flecha(
            x = __O,
            y = __S, 
            image = pygame.transform.rotate(self.imagemFlecha,135), 
            number = 2
        )
        self.flechaSL = flecha.Flecha(
            x = __L,
            y = __S, 
            image = pygame.transform.rotate(self.imagemFlecha,-135), 
            number = 3
        )

        self.flechaNL = flecha.Flecha(
            x = __L,
            y = __N, 
            image = pygame.transform.rotate(self.imagemFlecha,-45), 
            number = 4
        )
        self.next = sequencia.Sequencia(310, -200, self.imagemFlecha, 5)
    
    def run(self):
        # Mainloop
        relogio = pygame.time.Clock()
        while self.running:
            relogio.tick(60)
            # ----- Eventos -----
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.running = False
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        self.running = False
            
            # ----- Update -----
            self.flechaNO.update(self.superficie)
            self.flechaNL.update(self.superficie)
            self.flechaSO.update(self.superficie)
            self.flechaSL.update(self.superficie)

            self.next.update(self.superficie)


            # ----- Render -----
            self.superficie.fill((self.fundo))
            self.flechaNO.render(self.superficie)
            self.flechaNL.render(self.superficie)
            self.flechaSO.render(self.superficie)
            self.flechaSL.render(self.superficie)

            self.next.render(self.superficie)

            pygame.display.update()



if __name__ == "__main__":
    g = Jogo()
    g.run()

    pygame.quit()
    exit()
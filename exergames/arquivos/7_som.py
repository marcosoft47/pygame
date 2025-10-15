import pygame
import pygame.display
from pygame import mixer

pygame.init()

largura_tela = 630
altura_tela = 480
tela= pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('MEU PYANO - POR ANDRÉ BONETTO')

som_do = mixer.Sound('sons/do.mp3')
som_re = mixer.Sound('sons/re.mp3')
som_mi = mixer.Sound('sons/mi.mp3')
som_fa = mixer.Sound('sons/fa.mp3')
som_sol = mixer.Sound('sons/sol.mp3')
som_la = mixer.Sound('sons/la.mp3')
som_si = mixer.Sound('sons/si.mp3')

run = True

while run:

    som_do.play()
    pygame.time.delay(1000)
    som_re.play()
    pygame.time.delay(1000)
    som_mi.play()
    pygame.time.delay(1000)
    som_fa.play()
    pygame.time.delay(1000)
    som_sol.play()
    pygame.time.delay(1000)
    som_la.play()
    pygame.time.delay(1000)
    som_si.play()    
    
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            run=False
        
     
pygame.quit()
import pygame
from pygame import mixer
pygame.init()


telaAltura = 480
telaLargura = 640
keySize = 91

tela = pygame.display.set_mode((telaLargura, telaAltura))
pygame.display.set_caption('Meu Pyano - Marco Rigon')

fonte = pygame.font.SysFont("monocraft", 40, bold=True)

dano = pygame.mixer.Sound('sons/snd_hurt1.wav')
notas: dict[str, pygame.mixer.Sound] = {
    'do': mixer.Sound('sons/do.mp3'),
    're': mixer.Sound('sons/re.mp3'),
    'mi': mixer.Sound('sons/mi.mp3'),
    'fa': mixer.Sound('sons/fa.mp3'),
    'so': mixer.Sound('sons/sol.mp3'),
    'la': mixer.Sound('sons/la.mp3'),
    'si': mixer.Sound('sons/si.mp3')
}
figuras: dict[str, pygame.Surface] = {
    'vermelho': pygame.image.load('arquivos/figura_1_vermelho.png'),
    'amarelo': pygame.image.load('arquivos/figura_2_amarelo.png'),
    'verde': pygame.image.load('arquivos/figura_3_verde.png'),
}
cores : dict[str, tuple] = {
    'do': (0,0,0),
    're': (255,0,0),
    'mi': (0,255,0),
    'fa': (0,0,255),
    'so': (255,255,0),
    'la': (255,0,255),
    'si': (0,255,255)
}

roxo = (16,0,32)
corFundo = (0,0,0)

run = True
while run:
    # ----- Eventos ----
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            if e.key == pygame.K_1:
                notas['do'].play()
                corFundo = cores['do']
            if e.key == pygame.K_2:
                notas['re'].play()
                corFundo = cores['re']
            if e.key == pygame.K_3:
                notas['mi'].play()
                corFundo = cores['mi']
            if e.key == pygame.K_4:
                notas['fa'].play()
                corFundo = cores['fa']
            if e.key == pygame.K_5:
                notas['sol'].play()
                corFundo = cores['sol']
            if e.key == pygame.K_6:
                notas['la'].play()
                corFundo = cores['la']
            if e.key == pygame.K_7:
                notas['si'].play()
                corFundo = cores['si']
        if e.type == pygame.MOUSEBUTTONDOWN:
            dano.play()
    pos = pygame.mouse.get_pos()
    
    # ----- Update -----


    # ----- Renderiza --    
    pygame.draw.rect(tela, corFundo, [0,0, telaLargura, telaAltura])
    # pygame.draw.rect(tela, "red", [0,0, telaLargura, telaAltura//2])
    # pygame.draw.rect(tela, "white", [0,telaAltura//2, telaLargura,telaAltura])
    pygame.draw.line(tela, "white", (0, telaAltura//2), (telaLargura, telaAltura//2), 10)
    pygame.draw.ellipse(tela, "yellow", (20, 20, telaLargura-20, telaAltura//2-20), 5)
    # pygame.draw.circle(tela, "black",(telaLargura//2,telaAltura//2), 20)

    texto = fonte.render(str(pos), True, "white")

    pygame.draw.rect(tela, cores['do'], [keySize*0, telaAltura//2, keySize*1, telaAltura])
    pygame.draw.rect(tela, cores['re'], [keySize*1, telaAltura//2, keySize*2, telaAltura])
    pygame.draw.rect(tela, cores['mi'], [keySize*2, telaAltura//2, keySize*3, telaAltura])
    pygame.draw.rect(tela, cores['fa'], [keySize*3, telaAltura//2, keySize*4, telaAltura])
    pygame.draw.rect(tela, cores['so'], [keySize*4, telaAltura//2, keySize*5, telaAltura])
    pygame.draw.rect(tela, cores['la'], [keySize*5, telaAltura//2, keySize*6, telaAltura])
    pygame.draw.rect(tela, cores['si'], [keySize*6, telaAltura//2, keySize*7, telaAltura])

    tela.blit(texto, [20,20])

    pygame.display.flip()

pygame.quit()
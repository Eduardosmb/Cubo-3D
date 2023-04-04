import pygame 
import numpy
clock = pygame.time.Clock()


#faca o setup incial do pygame 
pygame.init()

#definir a largura e altura da tela
width, height = 600, 800

FPS = 60

#criar a tela
screen = pygame.display.set_mode((height, width))

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Controlar frame rate
    clock.tick(FPS)

    # Desenhar
    # desenhar uma linha

    pygame.draw.line(screen, (255, 0, 0), (200, 500), (500, 500), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 500), (200, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (500, 500), (500, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 200), (500, 200), 5)

    pygame.draw.line(screen, (255, 0, 0), (250, 250), (450, 250), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 250), (250, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 450), (450, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (450, 250), (450, 450), 5)


    pygame.draw.line(screen, (255, 0, 0), (250, 250), (250, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 250), (250, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 250), (250, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 250), (250, 450), 5)

    pygame.draw.line(screen, (255, 0, 0), (200, 500), (250, 450), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 250), (200, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (450, 250), (500, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (450, 450), (500, 500), 5)



    






    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)
    # pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 0), 5)

# (-0.5, -0.5, 0.5)
# (0.5, -0.5, 0.5)
# (-0.5, 0.5, 0.5)
# (0.5, 0.5, 0.5)
# (-0.5, -0.5, -0.5)
# (0.5, -0.5, -0.5)
# (-0.5, 0.5, -0.5)
# (0.5, 0.5, -0.5)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()
import pygame, sys

pygame.init()

pantalla_ancho = 750
pantalla_largo = 700

plomo = (29,29,27)

pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_largo))

pygame.display.set_caption("Python Invasores Espaciales")

reloj = pygame.time.Clock()

while True:
    # Comprovando los eventos
    for enento in pygame.event.get():
        if enento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Dibujando
    pantalla.fill(plomo)

    pygame.display.update()
    reloj.tick(60)
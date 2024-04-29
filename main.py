import pygame, sys
from nave import Nave

pygame.init()

pantalla_ancho = 750
pantalla_largo = 700

plomo = (29,29,27)

pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_largo))

pygame.display.set_caption("Python Invasores Espaciales")

reloj = pygame.time.Clock()

# Implementación nave
nave = Nave(pantalla_ancho, pantalla_largo)
grupo_nave = pygame.sprite.GroupSingle()
grupo_nave.add(nave)

while True:
    # Comprovando los eventos
    for enento in pygame.event.get():
        if enento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizando
    grupo_nave.update()

    # Dibujando
    pantalla.fill(plomo)
    grupo_nave.draw(pantalla)
    grupo_nave.sprite.grupo_lasers.draw(pantalla)

    pygame.display.update()
    reloj.tick(60)
import pygame, sys
from nave import Nave

pygame.init()

# Dimenciones de la pantalla
pantalla_ancho = 750
pantalla_largo = 700

# Color de fondo
plomo = (29,29,27)

# Creando la ventana de visualización
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_largo))

# Titulo de la ventana
pygame.display.set_caption("Python Invasores Espaciales")

# Controlar la velocidad de los fotogramas
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

    # Actualizar la posición de los objetos
    grupo_nave.update()

    # Dibujar en la pantalla
    pantalla.fill(plomo)
    grupo_nave.draw(pantalla)
    grupo_nave.sprite.grupo_lasers.draw(pantalla)

    # Actualizar pantalla
    pygame.display.update()
    reloj.tick(60)
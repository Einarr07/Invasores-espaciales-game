import pygame, sys
from juego import Juego

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

juego = Juego(pantalla_ancho, pantalla_largo)

while True:
    # Comprovando los eventos
    for enento in pygame.event.get():
        if enento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición de los objetos
    juego.grupo_nave.update()

    # Dibujar en la pantalla
    pantalla.fill(plomo)
    juego.grupo_nave.draw(pantalla)
    juego.grupo_nave.sprite.grupo_lasers.draw(pantalla)
    for obstaculo in juego.obstaculos:
        obstaculo.grupo_bloqueo.draw(pantalla)

    # Actualizar pantalla
    pygame.display.update()
    reloj.tick(60)
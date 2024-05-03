import pygame, sys, random
from juego import Juego

pygame.init()

# Dimensiones de la pantalla
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

# Crear una instancia de la clase Juego
juego = Juego(pantalla_ancho, pantalla_largo)

# Crear un evento para disparar láser
disparar_laser = pygame.USEREVENT
pygame.time.set_timer(disparar_laser, 300)

nave_misteriosa = pygame.USEREVENT + 1
pygame.time.set_timer(nave_misteriosa, random.randint(4000,8000))

while True:
    # Comprobar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == disparar_laser:
            juego.alien_laser()
        if evento.type == nave_misteriosa:
            juego.crear_nave_misteriosa()
            pygame.time.set_timer(nave_misteriosa, random.randint(4000,8000))

    # Actualizar la posición de los objetos
    juego.grupo_nave.update()
    juego.mover_aliens()
    juego.grupo_lasers_alien.update()
    juego.grupo_nave_misteriosa.update()

    # Dibujar en la pantalla
    pantalla.fill(plomo)
    juego.grupo_nave.draw(pantalla)
    juego.grupo_nave.sprite.grupo_lasers.draw(pantalla)
    for obstaculo in juego.obstaculos:
        obstaculo.grupo_bloqueo.draw(pantalla)
    juego.grupo_aliens.draw(pantalla)
    juego.grupo_lasers_alien.draw(pantalla)
    juego.grupo_nave_misteriosa.draw(pantalla)

    # Actualizar pantalla
    pygame.display.update()
    reloj.tick(60)

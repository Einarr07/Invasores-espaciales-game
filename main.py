import pygame, sys, random
from juego import Juego

pygame.init()

# Dimensiones de la pantalla
pantalla_ancho = 750
pantalla_largo = 700
balance = 50

# Color de fondo
plomo = (29,29,27)
amarillo = (243,216,63)

fuente = pygame.font.Font("Fuente/monogram.ttf", 40)
superficie_nivel = fuente.render("NIVEL 01", False, amarillo)
superficie_juego_terminado = fuente.render("FIN DEL JUEGO", False, amarillo)

# Creando la ventana de visualización
pantalla = pygame.display.set_mode((pantalla_ancho + balance, pantalla_largo + 2*balance))

# Titulo de la ventana
pygame.display.set_caption("Python Invasores Espaciales")

# Controlar la velocidad de los fotogramas
reloj = pygame.time.Clock()

# Crear una instancia de la clase Juego
juego = Juego(pantalla_ancho, pantalla_largo, balance)

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
        if evento.type == disparar_laser and juego.run:
            juego.alien_laser()
        if evento.type == nave_misteriosa and juego.run:
            juego.crear_nave_misteriosa()
            pygame.time.set_timer(nave_misteriosa, random.randint(4000,8000))

        claves = pygame.key.get_pressed()
        if claves[pygame.K_SPACE] and juego.run == False:
            juego.resetear()

    # Actualizar la posición de los objetos
    if juego.run:
        juego.grupo_nave.update()
        juego.mover_aliens()
        juego.grupo_lasers_alien.update()
        juego.grupo_nave_misteriosa.update()
        juego.verificar_colisiones()

    # Dibujar en la pantalla
    pantalla.fill(plomo)

    # Interfas de usuario
    pygame.draw.rect(pantalla, amarillo, (10,10,780,780), 2,0,60,60,60,60)
    pygame.draw.line(pantalla, amarillo, (25,730), (775,730), 3)
    if juego.run:
        pantalla.blit(superficie_nivel, (570,740,50,50))
    else:
        pantalla.blit(superficie_juego_terminado, (570,740,50,50))

    x = 50
    for vida in range(juego.lives):
        pantalla.blit(juego.grupo_nave.sprite.image, (x,745))
        x += 50

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

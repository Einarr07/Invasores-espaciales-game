import pygame, sys, random
from juego import Juego

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
pantalla_ancho = 750
pantalla_largo = 700
balance = 50

# Definir color de fondo
plomo = (29,29,27)
amarillo = (243,216,63)

# Cargar fuentes
fuente = pygame.font.Font("Fuente/monogram.ttf", 40)

# Crear superficies de texto
superficie_nivel = fuente.render("NIVEL 01", False, amarillo)
superficie_juego_terminado = fuente.render("FIN DEL JUEGO", False, amarillo)
texto_puntos = fuente.render("PUNTOS", False, amarillo)
texto_max_puntos = fuente.render("MAX PUNTOS", False, amarillo)

# Crear ventana de visualización
pantalla = pygame.display.set_mode((pantalla_ancho + balance, pantalla_largo + 2*balance))

# Establecer título de la ventana
pygame.display.set_caption("Python Invasores Espaciales")

# Controlar la velocidad de los fotogramas
reloj = pygame.time.Clock()

# Crear instancia de la clase Juego
juego = Juego(pantalla_ancho, pantalla_largo, balance)

# Crear evento para disparar láser
disparar_laser = pygame.USEREVENT
pygame.time.set_timer(disparar_laser, 300)

# Crear evento para crear nave misteriosa
nave_misteriosa = pygame.USEREVENT + 1
pygame.time.set_timer(nave_misteriosa, random.randint(4000,8000))

# Bucle principal del juego
while True:
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == disparar_laser and juego.run:
            juego.alien_laser()
        if evento.type == nave_misteriosa and juego.run:
            juego.crear_nave_misteriosa()
            pygame.time.set_timer(nave_misteriosa, random.randint(4000,8000))

        # Detectar pulsación de teclas
        claves = pygame.key.get_pressed()
        if claves[pygame.K_SPACE] and juego.run == False:
            juego.resetear()

    # Actualizar posiciones de los objetos
    if juego.run:
        juego.grupo_nave.update()
        juego.mover_aliens()
        juego.grupo_lasers_alien.update()
        juego.grupo_nave_misteriosa.update()
        juego.verificar_colisiones()

    # Dibujar en la pantalla
    pantalla.fill(plomo)

    # Dibujar interfaz de usuario
    pygame.draw.rect(pantalla, amarillo, (10,10,780,780), 2,0,60,60,60,60)
    pygame.draw.line(pantalla, amarillo, (25,730), (775,730), 3)
    if juego.run:
        pantalla.blit(superficie_nivel, (570,740,50,50))
    else:
        pantalla.blit(superficie_juego_terminado, (570,740,50,50))

    # Dibujar vidas
    x = 50
    for vida in range(juego.lives):
        pantalla.blit(juego.grupo_nave.sprite.image, (x,745))
        x += 50

    # Dibujar texto de puntos y puntuación
    pantalla.blit(texto_puntos, (50,15,50,50))
    formatear_puntos = str(juego.score).zfill(5)
    superficie_puntos = fuente.render(formatear_puntos, False, amarillo)
    pantalla.blit(superficie_puntos, (50,40,50,50))

    # Dibujar texto de puntos máximos y puntuación máxima
    pantalla.blit(texto_max_puntos, (550,15,50,50))
    formatear_max_puntos = str(juego.highscore).zfill(5)
    superficie_max_puntos = fuente.render(formatear_max_puntos, False, amarillo)
    pantalla.blit(superficie_max_puntos, (625,40,50,50))

    # Dibujar sprites
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
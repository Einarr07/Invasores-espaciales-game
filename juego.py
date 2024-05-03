import pygame, random
from nave import Nave
from obstaculos import Obstaculo, defensa
from alien import Alien
from laser import Laser
from alien import NaveMisteriorsa


# Definición de la clase Juego
class Juego:
    def __init__(self, pantalla_ancho, pantalla_largo):
        # Inicializar las dimensiones de la pantalla
        self.pantalla_ancho = pantalla_ancho
        self.pantalla_largo = pantalla_largo
        # Crear un grupo de sprites para la nave
        self.grupo_nave = pygame.sprite.GroupSingle()
        # Añadir una instancia de la clase Nave al grupo de la nave
        self.grupo_nave.add(Nave(self.pantalla_ancho, self.pantalla_largo))
        # Crear los obstáculos del juego
        self.obstaculos = self.crear_obstaculos()
        # Crear un grupo de sprites para los aliens
        self.grupo_aliens = pygame.sprite.Group()
        # Crear los aliens del juego
        self.crear_aliens()
        # Dirección inicial de los aliens
        self.direccion_aliens = 1
        # Crear un grupo de sprites para los lasers de los aliens
        self.grupo_lasers_alien = pygame.sprite.Group()
        #
        self.grupo_nave_misteriosa = pygame.sprite.GroupSingle()

    def crear_obstaculos(self):
        # Calcular el ancho total de los obstáculos
        obstaculos_ancho = len(defensa[0]) * 3
        # Calcular el espacio entre los obstáculos
        brecha = (self.pantalla_ancho - (4 * obstaculos_ancho)) / 5
        # Lista para almacenar los obstáculos
        obstaculos = []
        # Crear 4 obstáculos
        for i in range(4):
            # Calcular la posición x del obstáculo
            compensar_x = (i + 1) * brecha + i * obstaculos_ancho
            # Crear un obstáculo en la posición calculada y a una altura específica
            obstaculo = Obstaculo(compensar_x, self.pantalla_largo - 100)
            # Añadir el obstáculo a la lista de obstáculos
            obstaculos.append(obstaculo)
        # Devolver la lista de obstáculos
        return obstaculos

    def crear_aliens(self):
        # Crear los aliens en filas y columnas
        for fila in range(5):
            for columna in range(11):
                x = 75 + columna * 55
                y = 110 + fila * 55

                # Determinar el tipo de alien según la fila
                if fila == 0:
                    tipo_alien = 3
                elif fila in (1, 2):
                    tipo_alien = 2
                else:
                    tipo_alien = 1

                # Crear un alien en la posición calculada
                alien = Alien(tipo_alien, x, y)
                self.grupo_aliens.add(alien)

    def mover_aliens(self):
        # Mover los aliens en la pantalla
        self.grupo_aliens.update(self.direccion_aliens)
        aliens_grafico = self.grupo_aliens.sprites()
        for alien in aliens_grafico:
            # Cambiar de dirección si un alien alcanza los bordes de la pantalla
            if alien.rect.right >= self.pantalla_ancho:
                self.direccion_aliens = -1
                self.mover_aliens_abajo(2)
            elif alien.rect.left <= 0:
                self.direccion_aliens = 1
                self.mover_aliens_abajo(2)

    def mover_aliens_abajo(self, distancia):
        # Mover todos los aliens hacia abajo
        if self.grupo_aliens:
            for alien in self.grupo_aliens.sprites():
                alien.rect.y += distancia

    def alien_laser(self):
        # Disparar un laser desde un alien aleatorio
        if self.grupo_aliens.sprites():
            alien_random = random.choice(self.grupo_aliens.sprites())
            laser_grafico = Laser(alien_random.rect.center, -6, self.pantalla_largo)
            self.grupo_lasers_alien.add(laser_grafico)

    def crear_nave_misteriosa(self):
        self.grupo_nave_misteriosa.add(NaveMisteriorsa(self.pantalla_ancho))

    def verificar_colisiones(self):
        # Laser que dispara nuestro tanqu
        if self.grupo_nave.sprite.grupo_lasers:
            for laser_grafico in self.grupo_nave.sprite.grupo_lasers:
                if pygame.sprite.spritecollide(laser_grafico, self.grupo_aliens, True):
                    laser_grafico.kill()
                if pygame.sprite.spritecollide(laser_grafico, self.grupo_nave_misteriosa, True):
                    laser_grafico.kill()

                for obstaculo in self.obstaculos:
                    if pygame.sprite.spritecollide(laser_grafico, obstaculo.grupo_bloqueo, True):
                        laser_grafico.kill()

        # Laser que disparan los aliens
        if self.grupo_lasers_alien:
            for laser_grafico in self.grupo_lasers_alien:
                if pygame.sprite.spritecollide(laser_grafico, self.grupo_nave, False):
                    laser_grafico.kill()
                    print("Golpe nave")

                for obstaculo in self.obstaculos:
                    if pygame.sprite.spritecollide(laser_grafico, obstaculo.grupo_bloqueo, True):
                        laser_grafico.kill()

        if self.grupo_aliens:
            for alien in self.grupo_aliens:
                for obstaculo in self.obstaculos:
                    pygame.sprite.spritecollide(alien, obstaculo.grupo_bloqueo, True)
                    if pygame.sprite.spritecollide(alien, self.grupo_nave, False):
                        print("Golpe nave 2")


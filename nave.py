import pygame
from laser import Laser


# Definición de la clase Nave
class Nave(pygame.sprite.Sprite):
    def __init__(self, pantalla_ancho, pantalla_largo, balance):
        super().__init__()
        self.balance = balance
        self.pantalla_ancho = pantalla_ancho
        self.pantalla_largo = pantalla_largo
        self.image = pygame.image.load("Graficos/nave.png")
        self.rect = self.image.get_rect(midbottom=((self.pantalla_ancho + self.balance)/ 2, self.pantalla_largo))
        self.velocidad = 6
        self.grupo_lasers = pygame.sprite.Group()
        self.laser_listo = True
        self.laser_tiempo = 0
        self.laser_retraso = 300
        self.sonido_laser = pygame.mixer.Sound("Sonidos/laser.ogg")

    # Método para controlar la entrada del usuario
    def entrada_usuario(self):
        claves = pygame.key.get_pressed()

        if claves[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

        if claves[pygame.K_LEFT]:
            self.rect.x -= self.velocidad

        if claves[pygame.K_SPACE] and self.laser_listo:
            self.laser_listo = False
            laser = Laser(self.rect.center, 5, self.pantalla_largo)
            self.grupo_lasers.add(laser)
            self.laser_tiempo = pygame.time.get_ticks()
            self.sonido_laser.play()

    # Método para actualizar la posición y estado de la nave
    def update(self):
        self.entrada_usuario()
        self.restringir_movimiento()
        self.grupo_lasers.update()
        self.recarga_laser()

    # Método para restringir el movimiento de la nave dentro de la pantalla
    def restringir_movimiento(self):
        if self.rect.right > self.pantalla_ancho:
            self.rect.right = self.pantalla_ancho
        if self.rect.left < self.balance:
            self.rect.left = self.balance

    # Método para recargar el láser después de disparar
    def recarga_laser(self):
        if not self.laser_listo:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.laser_tiempo >= self.laser_retraso:
                self.laser_listo = True

    def resetear(self):
        self.rect = self.image.get_rect(midbottom = ((self.pantalla_ancho + self.balance)/2, self.pantalla_largo))
        self.grupo_lasers.empty()
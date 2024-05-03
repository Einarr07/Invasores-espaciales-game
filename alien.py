import pygame, random


# Definición de la clase Alien
class Alien(pygame.sprite.Sprite):
    def __init__(self, tipo, x, y):
        # Inicializar la clase Sprite de Pygame
        super().__init__()
        # Tipo de alien (1, 2 o 3)
        self.tipo = tipo
        # Cargar la imagen del alien según su tipo
        path = f"Graficos/alien_{tipo}.png"
        self.image = pygame.image.load(path)
        # Establecer la posición del rectángulo del alien en la pantalla
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direccion):
        # Actualizar la posición del alien moviéndolo en la dirección especificada
        self.rect.x += direccion


class NaveMisteriorsa(pygame.sprite.Sprite):
    def __init__(self, pantalla_ancho):
        super().__init__()
        self.pantalla_ancho = pantalla_ancho
        self.image = pygame.image.load("Graficos/misterio.png")

        x = random.choice([0, self.pantalla_ancho - self.image.get_width()])
        if x == 0:
            self.velocidad = 3
        else:
            self.velocidad = -3
        self.rect = self.image.get_rect(topleft = (x,40))

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.right > self.pantalla_ancho:
            self.kill()
        elif self.rect.left < 0:
            self.kill()

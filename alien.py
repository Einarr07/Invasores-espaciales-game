import pygame


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

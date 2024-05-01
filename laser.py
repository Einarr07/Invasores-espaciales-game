import pygame


# Definición de la clase Laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, posicion, velocidad, pantalla_altura):
        super().__init__()
        # Crear la imagen del láser
        self.image = pygame.Surface((4, 15))
        self.image.fill((243, 216, 63))  # Color del láser (amarillo claro)
        self.rect = self.image.get_rect(center=posicion)
        self.velocidad = velocidad
        self.pantalla_altura = pantalla_altura

    # Método para actualizar la posición del láser
    def update(self):
        self.rect.y -= self.velocidad  # Mover hacia arriba según la velocidad
        # Eliminar el láser si sale de la pantalla
        if self.rect.y > self.pantalla_altura + 15 or self.rect.y < 0:
            self.kill()

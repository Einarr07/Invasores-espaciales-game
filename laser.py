import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, posicion, velocidad, pantalla_altura):
        super().__init__()
        self.image = pygame.Surface((4,15))
        self.image.fill((243, 216, 63))
        self.rect = self.image.get_rect(center = posicion)
        self.velocidad = velocidad
        self.pantalla_altura = pantalla_altura

    def update(self):
        self.rect.y -= self.velocidad
        if self.rect.y > self.pantalla_altura + 15 or self.rect.y < 0:
            self.kill()
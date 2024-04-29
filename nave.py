import pygame


class Nave(pygame.sprite.Sprite):
    def __init__(self, pantalla_ancho, pantalla_largo):
        super().__init__()
        self.pantalla_ancho = pantalla_ancho
        self.pantalla_largo = pantalla_largo
        self.image = pygame.image.load("Graficos/nave.png")
        self.rect = self.image.get_rect(midbottom = (self.pantalla_ancho/2, self.pantalla_largo))
        self.velocidad = 6

    def entrada_usuario(self):
        clave = pygame.key.get_pressed()

        if clave[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

        if clave[pygame.K_LEFT]:
            self.rect.x -= self.velocidad

    def update(self):
        self.entrada_usuario()
        self.restringir_movimiento()

    def restringir_movimiento(self):
        if self.rect.right > self.pantalla_ancho:
            self.rect.right = self.pantalla_ancho
        if self.rect.left < 0:
            self.rect.left = 0
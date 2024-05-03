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


# Definición de la clase NaveMisteriorsa
class NaveMisteriorsa(pygame.sprite.Sprite):
    def __init__(self, pantalla_ancho, balance):
        super().__init__()
        # Ancho de la pantalla y balance como variables de instancia
        self.pantalla_ancho = pantalla_ancho
        self.balance = balance
        # Cargar la imagen de la nave misteriosa
        self.image = pygame.image.load("Graficos/misterio.png")

        # Elección aleatoria de la posición inicial de la nave
        x = random.choice([self.balance/2, self.pantalla_ancho + self.balance - self.image.get_width()])
        # Establecer la velocidad de la nave según su posición inicial
        if x == self.balance/2:
            self.velocidad = 3
        else:
            self.velocidad = -3
        # Establecer la posición del rectángulo de la nave en la pantalla
        self.rect = self.image.get_rect(topleft = (x,90))

    def update(self):
        # Actualizar la posición de la nave moviéndola según su velocidad
        self.rect.x += self.velocidad
        # Verificar si la nave ha salido de la pantalla por la derecha
        if self.rect.right > self.pantalla_ancho + self.balance/2:
            # Eliminar la nave del juego
            self.kill()
        # Verificar si la nave ha salido de la pantalla por la izquierda
        elif self.rect.left < self.balance/2:
            # Eliminar la nave del juego
            self.kill()
import pygame


# Definición de la clase bloqueo
class Bloqueo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3,3,))
        self.image.fill((245,216,63)) # Color amarillo
        self.rect = self.image.get_rect(topleft = (x,y))


# Matriz de defensa
defensa = [
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]


# Definición de la clase Obstaculo
class Obstaculo:
    def __init__(self, x, y):
        # Crear un grupo de sprites para los bloques de defensa
        self.grupo_bloqueo = pygame.sprite.Group()
        # Iterar sobre la matriz de defensa
        for fila in range(len(defensa)):
            for columna in range(len(defensa[fila])):
                # Si el valor en la matriz es 1, crear un bloque en la posición correspondiente
                if defensa[fila][columna] == 1:
                    # Calcular la posición del bloque
                    posicion_x = x + columna * 3
                    posicion_y = y + fila * 3
                    # Crear un bloque y añadirlo al grupo
                    bloqueo = Bloqueo(posicion_x, posicion_y)
                    self.grupo_bloqueo.add(bloqueo)

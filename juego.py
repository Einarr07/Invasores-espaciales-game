import pygame
from nave import Nave
from obstaculos import Obstaculo, defensa


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

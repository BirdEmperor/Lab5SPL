from art import *
from .Shape3D import Shape3D

class Cube(Shape3D):
    def __init__(self, size, color='white'):
        super().__init__(size, color)

    def transform_to_2d(self):
        size = self.size
        depth = self.depth_offset

        # Создаем ASCII-арт для куба
        art = []

        # Рисуем переднюю грань
        art.append('#' * size)  # верх
        for i in range(size - 2):
            art.append('#' + ' ' * (size - 2) + '#')  # боковые стороны
        art.append('#' * size)  # низ

        # Рисуем заднюю грань с смещением для создания эффекта объёма
        for i in range(depth):
            art.append(' ' * (depth - i - 1) + '#' * size)  # смещение

        return "\n".join(art)

    def display(self):
        # Используем art для вывода
        cube_art = self.transform_to_2d()
        print(cube_art)

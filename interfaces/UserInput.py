class UserInput:
    def get_shape_type(self):
        return input("Введите тип фигуры (например, 'cube'): ")

    def get_shape_size(self):
        size = int(input("Введите размер фигуры: "))
        return size

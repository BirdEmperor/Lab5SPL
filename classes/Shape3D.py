class Shape3D:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
        self.depth_offset = size // 5  # Определяем смещение для объёма

    def transform_to_2d(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе")

    def display(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе")

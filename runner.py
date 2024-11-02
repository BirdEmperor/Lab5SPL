from classes.Cube import Cube
from interfaces.UserInput import UserInput
from interfaces.Display import Display
from init import settings

def main():
    # Ввод пользователя
    user_input = UserInput()
    shape_type = user_input.get_shape_type()
    size = user_input.get_shape_size()

    # Создание и трансформация фигуры
    if shape_type.lower() == "cube":  # Исправлено: добавлены скобки
        shape = Cube(size)
    else:
        print("Неизвестная фигура.")
        return

    # Получение ASCII-арта
    ascii_art = shape.transform_to_2d()

    # Вывод ASCII-арта
    display = Display()
    display.show_ascii_art(ascii_art)

if __name__ == "__main__":
    main()

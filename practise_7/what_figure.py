# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

import simple_draw as sd

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)


color_print = int(input('Какой цвет вы хотите выбрать \n1 White \n2 Black \n3 Red \n4 Orange \n5 Green '
                        '\n6 Cyan \n7 Blue \n8 Purple \n'))


def color_type():
    if color_print == 1:
        return COLOR_WHITE
    elif color_print == 2:
        return COLOR_BLACK
    elif color_print == 3:
        return COLOR_RED
    elif color_print == 4:
        return COLOR_ORANGE
    elif color_print == 5:
        return COLOR_GREEN
    elif color_print == 6:
        return COLOR_CYAN
    elif color_print == 7:
        return COLOR_BLUE
    elif color_print == 8:
        return COLOR_PURPLE


def triangle(start_point=sd.get_point(480, 20), angle=0, length=100):
    for angle_1 in (0, 120, 240):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_1, length=length, width=2)
        v.draw(color_type())
        start_point = v.end_point


def rectangle(start_point=sd.get_point(20, 20), length=100, angle=0):
    for angle_ in (0, 90, 180, 270):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color_type())
        start_point = v.end_point


def five_angle(start_point=sd.get_point(250, 20), length=100, angle=0):
    for angle_ in (0, 72, 144, 216, 288):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color_type())
        start_point = v.end_point


def six_angle(start_point=sd.get_point(250, 300), length=100, angle=0):
    for angle_ in (0, 60, 120, 180, 240, 300):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color_type())
        start_point = v.end_point


type_figure = int(input('\n1 Треуголник \n2 Четыриугольник \n3 Пятиугольник \n4 Шестиугольник \n5 Все фигуры \n'))

if type_figure == 1:
    triangle(start_point=sd.get_point(250, 250))
elif type_figure == 2:
    rectangle(start_point=sd.get_point(250, 250))
elif type_figure == 3:
    five_angle(start_point=sd.get_point(250, 250))
elif type_figure == 4:
    six_angle(start_point=sd.get_point(250, 250))
elif type_figure == 5:
    triangle()
    rectangle()
    five_angle()
    six_angle()

if __name__ == "__main__":
    sd.pause()

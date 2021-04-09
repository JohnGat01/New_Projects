# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

import simple_draw as sd

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)

v = int(input('Какой цвет вы хотите выбрать \n1 White \n2 Black \n3 Red \n4 Orange \n5 Green '
              '\n6 Cyan \n7 Blue \n8 Purple \n'))


def color_type():
    if v == 1:
        return COLOR_WHITE
    elif v == 2:
        return COLOR_BLACK
    elif v == 3:
        return COLOR_RED
    elif v == 4:
        return COLOR_ORANGE
    elif v == 5:
        return COLOR_GREEN
    elif v == 6:
        return COLOR_CYAN
    elif v == 7:
        return COLOR_BLUE
    elif v == 8:
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


triangle()
rectangle()
five_angle()
six_angle()


sd.pause()

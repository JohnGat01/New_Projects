# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)
COLOR_YELLOW = (255, 255, 0)
point = sd.get_point(200, 200)
radius = 50
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
'''for i in range(3):
    radius += 5
    sd.circle(point, radius, COLOR_YELLOW, 2)
'''


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(point, radius, COLOR_YELLOW, 2)


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 200)
    bubble(point, 5)


# Нарисовать три ряда по 10 пузырьков
'''for y in range(200,501,100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point, 5)
'''

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point, 5)

sd.pause()

# -*- coding: utf-8 -*-
import simple_draw as sd
from random import randint
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
point = sd.get_point(0, 0)
point1 = sd.get_point(100, 50)


def wall(point, point1):
    sd.rectangle(point, point1, color=sd.COLOR_BLACK)


'''for i in range(0, 1000, 110):
    point = sd.get_point(i + 10, 0)
    point1 = sd.get_point(i + 110, 50)
    sd.rectangle(point, point1, color=sd.COLOR_BLACK)
'''

for y in range(0, 1000, 100):
    for i in range(0, 1000, 110):
        point = sd.get_point(i + randint(3, 8), y)
        point1 = sd.get_point(i +110, y + 85)
        sd.rectangle(point, point1, color=sd.COLOR_BLACK)


sd.pause()

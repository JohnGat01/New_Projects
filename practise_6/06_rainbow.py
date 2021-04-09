# -*- coding: utf-8 -*-
# (цикл for)
import simple_draw as sd
from random import choice

sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
radius = 500


def random_color():
    colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
              sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    return choice(colors)


for i in range(7):
    point = sd.get_point(500, 0)
    sd.circle(point, radius, random_color(), 20)
    radius += 20

sd.pause()

# -*- coding: utf-8 -*-
# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
radius = 500



for i in range(7):
    point = sd.get_point(500, 0)
    sd.circle(point, radius, rainbow_colors[i], 20)
    radius += 20

sd.pause()

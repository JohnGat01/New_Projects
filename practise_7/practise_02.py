# -*- coding: utf-8 -*-
import simple_draw as sd


def triangle(start_point=sd.get_point(480, 20), angle=0, length=100):
    for angle_1 in (0, 120, 240):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_1, length=length)
        v.draw(color=[255, 255, 255])
        start_point = v.end_point


def rectangle(start_point=sd.get_point(20, 20), length=100, angle=0):
    for angle_ in (0, 90, 180, 270):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color=[255, 255, 255])
        start_point = v.end_point


def five_angle(start_point=sd.get_point(250, 20), length=100, angle=0):
    for angle_ in (0, 72, 144, 216, 288):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color=[255, 255, 255])
        start_point = v.end_point


def six_angle(start_point=sd.get_point(250, 300), length=100, angle=0):
    for angle_ in (0, 60, 120, 180, 240, 300):
        v = sd.get_vector(start_point=start_point, angle=angle + angle_, length=length, width=2)
        v.draw(color=[255, 255, 255])
        start_point = v.end_point


triangle()
rectangle()
five_angle()
six_angle()


sd.pause()

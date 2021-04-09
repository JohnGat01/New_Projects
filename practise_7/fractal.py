# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

point_0 = sd.get_point(600, 0)
angle_0 = 90
length_0 = 200
# next_length = length_0
# next_angle = angle_0
# next_point = point_0


# def draw_branches(point, angle, length):
#         v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#         v.draw(color=[255, 255, 0])
#         return v.end_point
#
# while next_length > 10:
#     next_point = draw_branches(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * .80
# TODO
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v.draw(color=[255, 255, 0])
    next_point = v.end_point
    next_length = length * .75
    next_angle = angle - delta
    draw_branches(next_point, next_angle, next_length, delta)
    length_1 = 200
    if length_1 < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw(color=[255, 255, 0])
    next_point_1 = v1.end_point
    next_length_1 = length_1 * .75
    draw_branches(next_point_1, next_angle, next_length_1, delta)


draw_branches(point=point_0, angle=angle_0, length=length_0, delta=30)

# def new_branch(point, angle, length, delta):
#     v = sd.get_vector(start_point=point, angle=angle + delta, length=length, width=2)
#     v.draw(color=[255, 255, 0])
#     v1 = sd.get_vector(start_point=point, angle=angle - delta, length=length, width=2)
#     v1.draw(color=[255, 255, 0])
#     return v.end_point, v1.end_point
#
#
# for delta in range(40, 5, -2):
#     new_branch(point=point_0, angle=90, length=200, delta=delta)


draw_branches(point=point_0, angle=90, length=200, delta=30)
# draw_branches_1(point=point_0, angle=90, length=200, delta=30)


# 3) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

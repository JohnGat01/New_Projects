import simple_draw as sd
from simple_draw import *
from random import randint

sd.resolution = (800, 800)

x = [100, 700, 200, 150, 550, 340, 544, 656, 76, 564, 77, 43, 656, 432, 123, 545]
y = 700

while True:
    sd.clear_screen()
    point = sd.get_point(x[0], y)
    sd.snowflake(center=point, length=50, color=COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
    y -= randint(4, 15)
    if y < -50:
        break
    x[0] += randint(5, 20)

#     point_2 = sd.get_point(x[1], y[1])
#     sd.snowflake(center=point_2, length=30, color=COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
#     y[1] -= randint(2, 10)
#     if y[1] < -50:
#         break
#     x[1] -= randint(3, 12)
#     sd.sleep(0.1)
#
#     if sd.user_want_exit():
#         break


sd.pause()

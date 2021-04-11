import simple_draw as sd
from simple_draw import *

sd.resolution = (800, 800)

snow = []
for i in range(20):
    x = randint(100, 500)
    y = 700
    snow.append([x, y])

def snowfall(c):
    while True:
        for c in snow:
            point = sd.get_point(c[0], c[1])
            sd.snowflake(center=point, length=30, color=COLOR_WHITE, factor_a=0.6, factor_b=0.35,
                         factor_c=60)
            c[0] += randint(-10, 20)
            c[1] -= randint(2, 30)
            if c[1] < -50:
                break
        sd.sleep(0.2)
        sd.clear_screen()
        if sd.user_want_exit():
            break


snowfall(c=snow)

sd.pause()

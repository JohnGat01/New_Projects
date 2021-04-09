import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length = 200
point = sd.get_point(300, 300)

# v1 = sd.get_vector(start_point=point, angle=0, length=length, width=2)
# v1.draw(color=[255, 255, 255])
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=length, width=2)
# v2.draw(color=[255, 255, 255])
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=length, width=2)
# v3.draw(color=[255, 255, 255])

# определить функцию рисования треугольника из заданной точки с заданным наклоном


def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw(color=[255, 255, 255])

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=2)
    v2.draw(color=[255, 255, 255])

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=2)
    v3.draw(color=[255, 255, 255])


for i in range(0, 361, 30):
    triangle(point=point, angle=i)


sd.pause()

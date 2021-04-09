#!/usr/bin/env python3
# -*- coding: utf-8 -*-

radius = 42
pi = 3.1415926


def square_all():
    square = pi * (radius ** 2)
    print(round(square, 4))


def first():
    point = (23, 34)
    hypotenuse = ((point[0] ** 2 + point[1] ** 2) ** 0.5)
    if hypotenuse >= radius:
        print('True')
    else:
        print('False')


def second():
    point = (30, 30)
    hypotenuse = ((point[0] ** 2 + point[1] ** 2) ** 0.5)
    if hypotenuse >= radius:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    square_all()
    first()
    second()

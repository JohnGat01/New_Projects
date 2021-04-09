#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Есть словарь координат городов
from pprint import pprint
sites = {
    'Kyiv': (550, 370),
    'London': (510, 510),
    'New York': (480, 480),
}


# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = dict()

kyiv = sites['Kyiv']
london = sites['London']
new_york = sites['New York']

kyiv_london = ((kyiv[0] - london[0]) ** 2 + (kyiv[1] - london[1]) ** 2) ** .5
kyiv_ney_york = ((kyiv[0] - new_york[0]) ** 2 + (kyiv[1] - new_york[1]) ** 2) ** .5
london_new_york = ((london[0] - new_york[0]) ** 2 + (london[1] - new_york[1]) ** 2) ** .5


distances['Kyiv'] = {}
distances['Kyiv']['London'] = kyiv_london
distances['Kyiv']['New York'] = kyiv_ney_york


distances['New York'] = {}
distances['New York']['London'] = london_new_york
distances['New York']['Kyiv'] = kyiv_ney_york

pprint(distances)

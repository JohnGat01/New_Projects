#  ФУНКЦИЯ ПО ВЫЧИЧЛЕНИЮ числа факториала с ПОМОЩЬЮ РЕКУРСИИ'''
# n = int(input())
# def factorial(n):
#     if n == 1:
#         return 1
#     factorial_minus_one = factorial(n=n - 1)
#     return n * factorial_minus_one
#
# print(factorial(9))


# ФУНКЦИЯ ПО НАХОЖДЕНИЮ ЕЛЕМЕНТА В СЛОВАРЕ СЛОВАРЕЙ С ПОМОЩЬЮ РЕКУРСИИ
# html_dom = {
#     'html': {
#         'head': {
#             'title': 'Colobok'
#         },
#         'body': {
#             'h2': 'Hello!',
#             'div': 'You want to hear fairytale?',
#             'p': 'Ok :)'
#         }
#      }
# }
#
# def find_element(tree, element_name):
#     if element_name in tree:
#         return tree[element_name]
#     for key, sub_tree in tree.items():
#         if isinstance(sub_tree, dict):
#             result = find_element(tree=sub_tree, element_name=element_name)
#             if result:
#                 break
#     else:
#         result = None
#     return result
#
# res = find_element(tree=html_dom, element_name='p')
# print(res)

def print_them_all(*args, **kwargs):
    print('type:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('Positional argument:', i, arg)
    print()
    print('type:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('Named argument:', key, value)


print_them_all('Vasiliy', 'Vladimer', 25, name='Kolya', adress='Bagana 13b', years=25)

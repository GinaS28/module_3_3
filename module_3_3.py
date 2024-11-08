def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 0, c= True)
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [1.5, 'строка', True ]
values_dict = {'a': 3, 'b': 'str', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [2.5, 'str']
print_params(*values_list_2, 42)


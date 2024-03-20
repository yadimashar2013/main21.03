def print_params(params):
    print('Параметры двигателя:', params * 2)
    return print_params


print_params('Тип двигателя')
print_params('Расход топлива')
print_params('Марка топлива')
print_params('Расход масла')

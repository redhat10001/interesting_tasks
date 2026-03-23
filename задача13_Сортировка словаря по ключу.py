print('*' * 25)

"""Сортировка"""

def info_kwargs(**kwargs):
    my_dict = {key: value for key, value in kwargs.items()}
    sorted_list = sorted(my_dict.items(), key=lambda x: x[0]) # список кортежей
    print(sorted_list)

info_kwargs(first_name="John", last_name="Doe", age=33)

print()

def info_kwargs(**kwargs):
    my_dict = {key: value for key, value in sorted(kwargs.items())}
    print(my_dict)

info_kwargs(first_name="John", last_name="Doe", age=33)

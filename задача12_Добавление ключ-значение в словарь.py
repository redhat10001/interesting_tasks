print('*' * 25)

def create_actor(**kwargs):
    my_dict = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 47
    }
    my_dict.update(kwargs)

    return my_dict

actor = create_actor(height=190, movies=['Дедпул', 'Главный герой'])
print(actor)

print()

def create_actor(**kwargs):
    my_dict = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 47
    }

    for k, v in kwargs.items():
        my_dict[k] = v

    return my_dict

actor = create_actor(height=190, movies=['Дедпул', 'Главный герой'])
print(actor)

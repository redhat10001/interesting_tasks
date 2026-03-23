print('*' * 25)


def add_attrs(**set_kwargs):
    def decorator(func):
        # Функция inner будет оборачивать исходную функцию func
        @__import__('functools').wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        # Добавляем атрибуты к inner, а не к func
        for key, value in set_kwargs.items():
            setattr(inner, key, value)

        # Возвращаем обёрнутую функцию
        return inner

    return decorator


@add_attrs(hello='World', marks=[1, 2, 3], cash=100)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.hello)
print(add.marks)
print(add.cash)
print(getattr(add, 'ordered', None))

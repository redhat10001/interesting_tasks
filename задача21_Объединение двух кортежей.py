print('*' * 25)

'''Объединение двух кортежей'''

tuple1 = (('b', 1), ('a', 1), ('b', 1))
tuple2 = (('b', 4), ('d', 1))

# Преобразуем tuple1 в список
result = list(tuple1)

# Получаем последний элемент из tuple1
last_key, last_value = result[-1]

# Получаем первый элемент из tuple2
key2, value2 = tuple2[0]

# Если ключи одинаковые, суммируем значения
if last_key == key2:
    result[-1] = (last_key, last_value + value2)

# Добавляем остальные элементы из tuple2 в конец
result.extend(tuple2[1:])

# Преобразуем результат обратно в кортеж
result_tuple = tuple(result)
print(result_tuple)

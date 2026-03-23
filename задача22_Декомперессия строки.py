print('=' * 25)
'''
Декомпрессия конкретного значения
'''
import re

def decompress_string(compressed: str) -> str:
    match = re.fullmatch(r'([A-Za-z])(\d+)', compressed)
    if match:
        letter = match.group(1)  # Первая группа (буква)
        repeat_count = int(match.group(2))  # Вторая группа (число)
        return letter * repeat_count  # Повторяем букву n раз
    return compressed  # Если формат не совпал, возвращаем как есть

# Проверяем
assert decompress_string("a1000000") == "a" * 1000000  # Должно работать!
#print("Тест пройден!")  # Если ошибок нет, код правильный

'''
Декомпрессия любого значения
'''
import re

def decompress_string(compressed: str) -> str:
    pattern = re.compile(r'([A-Za-z])(\d+)')  # Ищем букву и число
    result = []  # Будем накапливать части строки

    for match in pattern.finditer(compressed):
        letter = match.group(1)  # Буква
        repeat_count = int(match.group(2))  # Число
        result.append(letter * repeat_count)  # Добавляем повторенную букву

    return "".join(result)  # Объединяем список в строку

# Проверяем
assert decompress_string("a1b1c1d1e1f1g1h1i1j1k1w10000") == "abcdefghijk" + "w" * 10000
print("Тест пройден!")

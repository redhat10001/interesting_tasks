print('*' * 25)

# Чтение нескольких строк, например, пока не будет пустой строки
lines = []
while True:
    line = input()  # Считываем строку
    if not line:  # Если строка пустая, выходим из цикла
        break
    lines.append(line.split())  # Разделяем строку по пробелам и добавляем в список

print(lines)

print('-' * 25)

# Если хочешь ограничить количество строк
# (например, 5 строк), просто добавь счётчик:
lines = []
for _ in range(5):
    line = input()
    lines.append(line.split())

print(lines)

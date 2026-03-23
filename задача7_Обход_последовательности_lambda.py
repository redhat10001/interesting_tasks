print('*' * 25)
s = ['Hristophor', 'Ademar', 'Tey', 'Andrey', 'Aleksandr']

rez = filter(lambda name: name.startswith('A'), s)
print(*rez)

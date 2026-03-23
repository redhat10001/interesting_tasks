print('*' * 25)


s = [5, 3, 2, 1, 7, 2, 3, 5, 7]

new_s = list(dict.fromkeys(s).keys())

print(new_s)
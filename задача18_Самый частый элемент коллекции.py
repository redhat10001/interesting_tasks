print('*' * 25)


s = [1, 2, 3, 5, 7, 2, 3, 5, 7, 3, 5, 7, 5, 7, 5]

nvp = max(set(s), key=s.count)

print(nvp)
value = [151868, 153982, 156393]
s = []

for i in range(1, len(value)):
    res = value[i] - value[i - 1]
    s.append(res)
print(s)

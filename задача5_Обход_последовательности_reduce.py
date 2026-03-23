print('*' * 25)
from functools import reduce

rez = reduce(lambda x, y: x * y, map(int, input().strip().split()))
print(rez)

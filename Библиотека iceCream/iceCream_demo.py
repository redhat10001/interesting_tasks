
from icecream import ic
ic.configureOutput(prefix='Debug | ')

def square_of(num):
    return num*num
ic.enable() # Чтобы отключить указать disable()
num = 2
square_of_num = square_of(ic(num))
if ic(square_of_num) == pow(num, 2):
     print('Правильно')


vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

vector_new = [j for i in vector for j in i]
ic(vector_new)
# print(vector_new)
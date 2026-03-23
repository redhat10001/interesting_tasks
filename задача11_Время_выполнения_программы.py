print('*' * 25)

'''
В этом примере функция datetime.now() возвращает текущее дату и время, 
а разница между конечным и начальным временем вычисляется как разность 
между двумя объектами datetime.
'''

from datetime import datetime

start_time = datetime.now()  # время начала выполнения

# ваш код

end_time = datetime.now()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time} секунд")


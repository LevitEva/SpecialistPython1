# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
print('\m')

from random import randint

m = randint(5, 15)
random_list = [randint(-100, 100) for i in range(m)]
print(random_list)

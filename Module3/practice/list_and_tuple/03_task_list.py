# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
my_list=[1,7,6,5,-4,-3]
summa=0
for el in my_list:
    summa = summa + el
    print(summa)
    print(sum(my_list))

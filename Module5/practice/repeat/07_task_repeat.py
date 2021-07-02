# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.

def deposit(x, a, n):
    pass
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.
def last_page(num_items, items_on_page):
    last_items = num_items % items_on_page
    if last_items == 0:
        last_items = items_on_page
    return last_items


print(last_page(123, 10))
print(last_page(120, 10))

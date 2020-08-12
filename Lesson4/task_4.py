"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(timeit.timeit("func_1", "from __main__ import func_1"))
print(timeit.timeit("func_2", "from __main__ import func_2"))


def func_3():
    r_dict = {i:array.count(i) for i in array}
    max_value = max(r_dict.values())
    r_max_key = int(''.join([str(k) for k, v in r_dict.items() if v == max_value]))
    return f'Чаще всего встречается число {r_max_key}, ' \
           f'оно появилось в массиве {max_value} раз(а)'

print(timeit.timeit("func_3", "from __main__ import func_3"))

"""Разные тесты показывают разный результат, иногда моя функция обновняет другие, иногда нет"""
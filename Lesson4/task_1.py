"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


setup = "from __main__ import func_1"

time1 = timeit.timeit("func_1(range(20))", setup)


def func_2(nums):
	"""Я формировал список через генераторное выражение,
	   потому что это более лаконично и быстрее"""
	new_arr = [i for i in nums if i % 2 == 0]
	return new_arr


setup1 = "from __main__ import func_2"

time2 = timeit.timeit("func_2(range(20))", setup1)

if time1 < time2:
	print('First func faster')
else:
	print('Second func faster')
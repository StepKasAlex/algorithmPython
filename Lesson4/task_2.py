"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


time1 = timeit.timeit("recursive_reverse(126)", "from __main__ import recursive_reverse")


def recursive_reverse1(number):
	"""Сделал через ф-ию sorted, т.к. она быстрее
	   Также я сделал ф-ию, которая отличается от тех, которые в 3 задании"""
	s_num = list(str(number))
	n_num = int(''.join(sorted(s_num, reverse=True)))
	return n_num


time2 = timeit.timeit("recursive_reverse1(126)", "from __main__ import recursive_reverse1")

if time1 < time2:
	print('First faster')
else:
	print('Second faster')
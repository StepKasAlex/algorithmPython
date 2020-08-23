"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit

default_list = [1, 2, 3, 4, 5]
deq = deque(default_list)

def func1():
	deq.append(6)

def func1_1():
	default_list.append(6)

def func2():
	deq.extend(list(range(50)))

def func2_2():
	default_list.extend(list(range(50)))

def func3():
	deq.pop()

def func3_3():
	default_list.pop()


time1 = timeit('func1()', 'from __main__ import func1')
time2 = timeit('func1_1()', 'from __main__ import func1_1')
time3 = timeit('func2()', 'from __main__ import func2')
time4 = timeit('func2_2()', 'from __main__ import func2_2')
time5 = timeit('func3()', 'from __main__ import func3')
time6 = timeit('func3_3()', 'from __main__ import func3_3')

if time1 < time2:
	print('DEQUE WIN')
else:
	print('DEQUE LOSE')
"""Тут deque проиграл"""

if time3 < time4:
	print('DEQUE WIN')
else:
	print('DEQUE LOSE')
"""Тут deque выйграл"""

if time5 < time6:
	print('DEQUE WIN')
else:
	print('DEQUE LOSE')
"""Тут deque выйграл"""

"""В целом можно сказать, что деки работают быстрее при сложных и объемных операциях"""
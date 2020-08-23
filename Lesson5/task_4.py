"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict

n_dict = {'Apple' : 'IOS', 'Google' : 'Andriod', 'Microsoft' : 'Windows'}
odict = OrderedDict(n_dict)

def func1():
	odict.get('Apple')

def func1_1():
	n_dict.get('Apple')

def func2():
	odict.values()

def func2_2():
	n_dict.values()



time1 = timeit('func1()', 'from __main__ import func1')
time2 = timeit('func1_1()', 'from __main__ import func1_1')
time3 = timeit('func2()', 'from __main__ import func2')
time4 = timeit('func2_2()', 'from __main__ import func2_2')


if time1 < time2:
	print('OrderedDict WIN')
else:
	print('OrderedDict LOSE')
"""Тут OrderedDict выйграл"""

if time3 < time4:
	print('OrderedDict WIN')
else:
	print('OrderedDict LOSE')
"""Тут OrderedDict выйрал"""

"""OrderedDict побеждает"""
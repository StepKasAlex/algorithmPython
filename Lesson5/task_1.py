"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import Counter, defaultdict

def func():
	cmp_list = []
	cmp_dict = defaultdict(list)
	companies_num = int(input())
	companies_low = []
	companies_high = []
	for i in range(companies_num):
		name = input()
		money = list(map(int, input('Через пробел введите прибыль данного предприятия: ').split()))
		for m in money:
			cmp_list.append((name, m))
	for k, v in cmp_list:
		cmp_dict[k].append(v)
	sum_ = 0
	for v in cmp_dict.values():
		sum_ += sum(v)
	print('Средняя годовая прибыль всех предприятий: ', sum_ / companies_num)
	for k, v in cmp_dict.items():
		if sum(v) >= (sum_ / companies_num):
			companies_high.append(k)
		else:
			companies_low.append(k)
	print('Предприятия, с прибылью выше среднего значения: ', companies_high)
	print('Предприятия, с прибылью ниже среднего значения: ', companies_low)


func()
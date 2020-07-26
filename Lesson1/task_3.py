"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


dct = {'Apple' : 12, 'Samsung' : 8, 'Aliexspress' : 10, 'Nokia' : 1}

#  Сложность O(N logN)
def first_three1(dict_):
	return sorted(dict_.items(), reverse=True, key=lambda v: v[1])[:3]


print(first_three1(dct))


#  Сложность O(N**2)
def first_three2(dict_):
	dict1 = {}
	three_values = sorted([v for v in dict_.values()], reverse = True)[:3]
	for k in dict_.keys():
		for v in three_values:
			if dict_[k] == v:
				dict1[k] = v
	return dict1 

print(first_three2(dct))


#  Первый способ лучше, потому что по асимптотической нотации имеет наилучшую оценку (nlogn),
# которая с увеличением количества входных данных меньше увеличивает время вычисления 
	
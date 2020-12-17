"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

1) -1.5
2) +0.75
3) -0.375

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def summ(n, cnt = 1, num = 1, summa = None):
	if n != 0:
		if cnt == 1:
			summa = num
			cnt += 1
			n -= 1
			summ(n, cnt, num, summa)
		elif cnt % 2 != 0 and cnt != 1:
			num = num / -2
			summa += num
			cnt += 1
			n -= 1
			summ(n, cnt, num, summa)
		elif cnt % 2 == 0:
			num = num / -2
			summa += num
			cnt += 1
			n -= 1
			summ(n, cnt, num, summa)
	elif n == 0:
		print(summa)
		return None

summ(10)
# summ(int(input('Введите n: '))) Это если по заданию
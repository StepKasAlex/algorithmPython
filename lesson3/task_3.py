"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

def diff_substr(): 
	s_1 = 'papapapa'
	subs_lst = set()
	for i in range(len(s_1)):
		for j in range(i,len(s_1)):
			subs_lst.add(hashlib.sha256(s_1[i:j+1].encode('utf-8')).hexdigest())
	return len(subs_lst)

print(diff_substr())
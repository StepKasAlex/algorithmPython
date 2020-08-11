"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
from uuid import uuid4


def log_in():
	passwd = input()
	salt = uuid4().hex
	h_passwd1 = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
	passwd = input()
	h_passwd2 = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
	if h_passwd1 == h_passwd2:
		return 'Вы успешно зашли'

print(log_in())
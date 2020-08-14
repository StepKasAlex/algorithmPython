"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

class Web_Cash:
	def __init__(self):
		self.list_ = []
		self.salt = uuid4().hex
		self.get_url()

	def get_url(self):
		self.url = input()
		self.hashing_url()

	def hashing_url(self):
		self.hash_url = hashlib.sha256(self.salt.encode() + self.url.encode()).hexdigest()
		self.check_url()

	def add_url_list(self):
		self.list_.append(self.hash_url)

	def check_url(self):
		if self.hash_url not in self.list_:
			print('Nice')
			self.add_url_list()
		else:
			print('Not nice')
		self.get_url()


test = Web_Cash()
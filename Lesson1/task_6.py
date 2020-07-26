"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class TaskDesk:
	def __init__(self):
		self.basic = []
		self.revision = []

	def add_task(self, task):
		self.basic.append(task)

	def add_task_revision(self, rev):
		self.revision.append(rev)

	def get_task(self):
		task = self.basic[-1]
		self.pop_task()
		return task

	def get_rev(self):
		rev = self.revision[-1]
		self.pop_rev()
		return rev

	def pop_task(self):
		self.basic.pop()

	def pop_rev(self):
		self.revision.pop()

tasks = TaskDesk()
tasks.basic = [1, 2, 3, 4, 5]
print(tasks.get_task())
print(tasks.get_task())
print(tasks.get_task())
print(tasks.get_task())





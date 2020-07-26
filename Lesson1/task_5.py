"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class PlatesStack:
	def __init__(self):
		self.max_plates = 5
		self.shelf = []
		self.stack = None

	def create_ex(self):
		stack = PlatesStack()
		return stack

	def add_plate(self, plate):
		if self.stack == None:
			if(len(self.shelf) < self.max_plates):
				self.shelf.append(plate)
			elif(len(self.shelf) == self.max_plates):
				self.stack = self.create_ex()
		else:
			if(len(self.shelf) < self.max_plates):
				self.shelf.append(plate)
			elif(len(self.shelf) == self.max_plates):
				self.stack = self.create_ex()

stack = PlatesStack()
stack.add_plate(1)
stack.add_plate(1)
stack.add_plate(1)
stack.add_plate(1)
stack.add_plate(1)
stack.add_plate(1)

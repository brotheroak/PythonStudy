class Human():
	'''인간'''
	def __init__(self, name, weight):
		'''초기화 함수'''		
		self.name = name
		self.weight = weight		
		
	def __str__(self):
		'''문자열화 함수'''
		return "{}(몸무게 {}kg)".format(self.name, self.weight)
		
	def eat(self):
		self.weight += 0.1
		print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
		
	def walk(self):
		self.weight -= 0.1
		print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

person = Human("사람","73")
print(person)
class dequeue:
	def __init__(self, s):
		self.items = list(s)
		self.front_index = 0
	def append(self, c):
		self.items.append(c)
	def appendleft(self, c):
		self.items.insert(0, c)
	def pop(self):
		try:
			return self.items.pop()			
		except IndexError:
			print("dequeue is empty")
	def popleft(self):
		if len(self.items) == 0:
			print("dequeue is empty")
		else:
			left = self.items[self.front_index]
			self.front_index += 1
			return left
	def __len__(self):
		return len(self.items) - self.front_index
	def right(self):
		return self.items[-1]
	def left(self):
		return self.items[0]
	def __len__(self):
		return len(self)
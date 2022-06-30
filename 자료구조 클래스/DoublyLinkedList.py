class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self
		self.prev = self# 1. class Node 선언 부분

# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
	def __init__(self):
		self.head = Node("h")
		self.size = 0
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while v.next.key is not 'h':
			print(v.key, end=" -> ")
			v = v.next
		print(v.key,"->",self.head.key)	
		
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return									
		a.prev.next = b.next
		b.next.prev = a.prev #cut
	
		x.next.prev = b
		b.next = x.next
		a.prev = x 
		x.next = a		

	def moveAfter(self, a, x):
		self.splice(a, a, x)
		self.size += 1
		
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
		self.size += 1
		
	def insertBefore(self, x, key):
		a = Node(key)
		self.moveBefore(a, x)
			
	def insertAfter(self, x, key):
		a = Node(key)
		self.moveAfter(a, x)
		
	def pushFront(self, key):
		x = self.head
		self.insertAfter(x, key)
		
	def pushBack(self, key):
		x = self.head
		self.insertBefore(x, key)
		
	def deleteNode(self, x):	
			if x == None or x == self.head:
				return
			x.prev.next = x.next
			x.next.prev = x.prev
			del x
			self.size -= 1
		
	
	def popFront(self):
			x = self.head.next
			key = x.key
			if key == 'h':
				return None
			else:
				self.deleteNode(x)
				return key
	
	def popBack(self):
			x = self.head.prev
			key = x.key
			if key == 'h':
				return None
			else:
				self.deleteNode(x)
				return key
		
	def search(self, key):
		v = self.head
		while v.next != self.head:
			if v.key == key:
				return v
			v = v.next
		if v.key == key:
			return v
		else:
			return None	
		
	def first(self):
		if self.__len__ == 0 or self.head.next.key == 'h':
			return None
		else:
			return self.head.next.key
		
	def last(self):
		if self.__len__ == 0 or self.head.prev.key == 'h':
			return None
		else:
			return self.head.prev.key
		
	def isEmpty():
		if self.__len__ == 0:
			return True
		else:
			return False			
	
	def size(self):
		return self.size	
	def __len__(self):
		return self.size
		
	def join(self, l):
		for i in range(len(l)):
			self.pushBack(l[i])
	
	def split(self, x):
		p=[]
		l=[]
		h = self.head.next
		xp = x.prev
		xn = x.next
		while h != x:
			p.append(h.key)
			h = h.next
		h = h.next
		while h != self.head:
			l.append(h.key)
			h = h.next
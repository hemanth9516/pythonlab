class test:
	h=0
	def __init__(self):
		self.h=6

	def my_func(self,k):
		print("hi,im in class")
		self.h=k
		print(self.h)
o=test()
print(o.h)
o1=test()		
print(o1.h)
o.my_func(2)
print(o.h)
o1.my_func(8)
print(o1.h)

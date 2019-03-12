try:
	l=[1,2,3,4]
	a=int(input("enter a number"))
	if a>4:
		raise TypeError
	elif a<=5:
		raise NameError

except TypeError:
	print("Type error ,ur choice should be less than 5")
except NameError:
	print("name error ,ur choice is out of range")	
finally:
	print("excution complete")	

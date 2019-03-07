def func(num1,num2,num3):
	if (num1 >= num2) and (num1 >= num3):
   		return num1
	elif (num2 >= num1) and (num2 >= num3):
   		return num2
	else:
   		return num3
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c= float(input("Enter third number: "))
largest=func(a,b,c)
print(largest)

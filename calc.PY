def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select the options")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice=(input("enter the choice(1,2,3,4):"))
num1=int(input("enter the first number :"))
num2=int(input("enter the second number:"))
if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
else if choice=='2':
	print(num1,"-",num2,"=",substract(num1,num2))
else if choice=='3':
	print(num1,"*",num2,"=",multiply(num1,num2))
else if choice=='4':
	print(num1,"/",num2,"=",divide(num1,num2))
else:
	print("invalid input")

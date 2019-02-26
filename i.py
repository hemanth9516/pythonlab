import random
	
d=	0
p=	0
snl=[8:37,13:37,40:68,52:81,76:97,11:2,25:4,38:9,65:46,89:70,93:64]

while	True:
	r=	input("press r to roll the q to quit:")

	if	r=='r':
		d=	random.randint(1,6)
		print("you got :",d)
		if	d==	6:
			print("congratulations you can play the game now")
			break
		else:
			print("roll the die once again till you get 6")

while	True:
		r=	input("press r to roll q to quit:")

		if r==	'r':
			d=	random.randint(1,6)
			print("you got :",d)

			p=	p+d
			if	p > 100:
				p=p-d
				print("wait till you get ",100-p,"or less.")

			print("your new position is : ",p)

			if p==100:
				print("you win")
				exit()
			if p in snl:
				if p<snl[i]:
					print("wow you got lader:",)
				else:
					print("wow you got bite by snake ")
				p=snl[p]
				print("move to:",p)			
		elif	r=='q':
			print("bye")
			exit()														
													

import random
l=['r','p','s']
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0
while True:
	u=input("enter your choice,press n to discontinue ")
	if u=='n':
		print("game over")
		print("computer score",cs)
		print("user score",us)
		if us<cs:
			print("computer wins")
		elif us==cs:
			print("its tie")	
		else :
			print("user wins")		
		exit()
	c=random.choice(l)
	print("computer chooses ",d[c])
	print("user chooses",d[u])
	if u==c:
		print("tie")
	elif u=='r' and c=='p':
		print("computer wins")
		cs=cs+1
	elif u=='r'	and c=='s':
		print("you win")
		us=us+1
	elif u=='p' and c=="r":
		print("you win")
		us=us+1
	elif u=='p' and c=='s':
		print("computer wins")
		cs=cs+1
	elif u=='s' and c=='r':
		print("computer wins")
		cs=cs+1
	elif u=='s' and	c=='p':
		print("you win")
		us=us+1
	



		
		
			
		 		

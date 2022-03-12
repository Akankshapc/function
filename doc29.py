def nbr(x):
	i=0
	while i<=x:
		if i%2==0:
			print(i,"even")
		else:
			print(i,"odd")
		i+=1
a=int(input("enter limit"))
nbr(a)

#5#
def fact():
	a=int(input("enter nmbr"))
	fact=1
	while a>0:
		fact=fact*a
		a=a-1
	print("factorial",fact)
fact()


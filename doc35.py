#35 doc
def age(x):
	if x<=14:
		print("kids drink toddy")
	elif 18<=x<=20:
		print("teens drink coke")
	elif x<=21:
		print("young adults drink beer")
	elif x>21:
		print("adult drink whiskey")
a=int(input("enter age"))
age(a)

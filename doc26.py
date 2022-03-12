#26 doc#
def Fizz_Buzz():
	if a%3==0:
		print("Fizz")
	if a%5==0:
		print("Buzz")
	if a%3==0 and a%5==0:
		print("FizzBuzz")
	else:
		print(a)
a=int(input("enter nmbr"))
Fizz_Buzz()


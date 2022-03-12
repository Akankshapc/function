#MAXIMUM NUMBER#

def max(a,b,c):
	if b<a>c:
		print(a,"is max nmbr")
	if a<b<c:
		print(b,"is max nmbr")
	if b<c<a:
		print(c,"is max nmbr")
	else:
		print("equal")
x=int(input("enter nmbr"))
y=int(input("enter nmbr"))
z=int(input("enter nmbr"))
max(x,y,z)

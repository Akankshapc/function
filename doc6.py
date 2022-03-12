#6
def list(x):
	i=0
	b=[]
	while i<len(x):
		if x[i] not in b:
			b.append(x[i])
			print(b)
		i+=1
a=["rishabh","rishabh","abhishek","rishabh","divyashish","divyashish"]
list(a)

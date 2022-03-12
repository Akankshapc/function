#MAX, MIN#
def list(x):
	i=0
	max=0
	min=0
	while i<len(x):
		if (len(x[i]))>max:
			max=len(x[i])
			min=x[i]
			print(max,min)
		i+=1
a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
list(a)

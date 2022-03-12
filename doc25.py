#25 doc#
def list(x):
	a=[]
	b=[]
	i=0
	while i<len(x):
		if x[i]<0:
			b.append(x[i])
		if x[i]>0:
			a.append(x[i])
		i+=1
	print('negative',b)
	print('positive',a)
k=[2,-7,5,-64,-14]
list(k)

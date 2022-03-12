#facebook
def founder():
	a=['whobis founder of face book']
	b=[['Mark Zuckerberg','Bill Gates','Steve jobes','larry page']]
	c=[1]
	i=0
	count=0
	while i<len(a):
		print('your',i+1,'question')
		print(i+1,a[i])
		print('your option')
		j=0
		while j<len(b[i]):
			print(j+1,b[i][j])
			j+=1
		n=int(input('entr nbr'))
		if n==c[i]:
			print('congtrs')
		else:
			print('wrong ansr')
			break
		i+=1
	print('game ovr')
founder( )

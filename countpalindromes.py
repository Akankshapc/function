#counting the palindromes in the list#
def pali():
	a=["asd","aba","121","929","dae","CAC"]
	i=0
	c=0
	while i<len(a):
		if a[i]==a[i][::-1]:
			c+=1
		i+=1
	print(c)
pali()


#sum of digits##
def digits(nmbr):
    sum = 0
    b = 0
    while nmbr!=0 :
        b = nmbr%10
        sum+=b;
        nmbr=nmbr//10
    return sum
a=int(input('entr nbr'))
print(digits(a))

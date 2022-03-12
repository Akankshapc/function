def speed(speed):
	if speed<=70:
		print("ok")
	elif speed>=70:
		points=(speed-70)//5
		print(points)
		if points>=12:
			print("liscense suspected")
b=int(input("enter speed"))
speed(b)


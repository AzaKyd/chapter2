number = int(input("Input number: "))
square = 0
for i in range(0, number):
	square = i**2
	if number <= square:
		break
	print(square)
	

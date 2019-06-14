a = int(input("Input number A"))
b = int(input("Input number B"))

if a <= b:
	for i in range (a, b):
		print(i)
		if i == b - 1:
			print(b)

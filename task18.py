age = int(input("Input your age: "))


for i in range(1, age):
	if age % 2 == 0:
		if i % 2 == 0:
			print(i)
	else:
		if i % 2 != 0:
			print(i)

	

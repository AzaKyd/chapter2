some_string = input("Input String: ")

#1
if len(some_string) > 2:
	print(some_string[2])

#2
if len(some_string) > 1:
	print(some_string[-2])

#3
print(some_string[:5])

#4
print(some_string[:len(some_string)-2])

#5
for i in range(0, len(some_string), 2):
	print(some_string[i], end = '')
	print()

#6
for i in range(1, len(some_string), 2):
	print(some_string[i], end = '')
	print()

#7
print(some_string[::-1])

#8
for i in range(0, len(some_string), 2):
	liverpool = 0
	if liverpool == 0:
		reverse_string = some_string[::-1]
	print(reverse_string[i], end = '')
print()
#9
print(len(some_string))
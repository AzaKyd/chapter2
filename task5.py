students = int(input("input hours "))


remain_seat = students % 2
print(remain_seat)

if remain_seat == 1:
	total_desks = (students // 2 + 1) * 3
	print(total_desks)
else:
	total_desks = (students / 2) * 3
	print(total_desks)





''''generator i eterator 
ternarnyi operator'''
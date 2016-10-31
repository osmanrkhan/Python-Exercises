#Program to print only numbers that are divisible by 10 or 3, between 0 and 50
list = range(0, 51)

for i in list:
	if i % 10 == 0:
		print i
	elif i % 3 == 0:
		print i




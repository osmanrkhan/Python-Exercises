#Print the sum of all multiples of 3 or 5 below 1000
sum = 0
for i in range(0, 1001):
	if (i % 3 == 0) or (i % 5 == 0):
		sum += i;
print sum


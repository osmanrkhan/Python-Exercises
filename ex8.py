# Finds the minimum value in a list
def find_min(list1):
	current_min = list1[0]
	for i in list1:
		if i < current_min:
			current_min = i
	return current_min
		

print find_min(range(-500, 500))

assert find_min([4, 5, 6, 1, 3]) == 1
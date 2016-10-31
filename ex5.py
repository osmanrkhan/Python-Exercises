#Prints all numbers in a list less than five

def print_all_less_than_five(list1):
	for i in list1:
		if(i < 5):
			print i

examplelist = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_all_less_than_five(range(0, 500))

print_all_less_than_five(examplelist)

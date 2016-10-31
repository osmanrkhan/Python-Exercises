# def find_2min(list):
# 	print list.pop(1)

# find_2min(range(5, 50))

def listsorter(list1):
	curr_min = list1[0]
	sorted_list = []
	while len(list1) > 0:
		for i in list1:
			if i < curr_min:
				curr_min = i
		sorted_list.append(i)
		list1.remove(i)
	print sorted_list[0]

listsorter([8, 9, 5, 2, 77, 3, -4, -8, 9])


		

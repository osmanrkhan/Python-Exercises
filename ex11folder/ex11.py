filename = 'sample2.txt'

def return_with_line_numbers(filename):
	with open(filename, 'r') as myfile:

		i = 1
		to_return = []
		for line in myfile:
			to_return.append(str(i) + " " + line.strip())
			i += 1 # shortcut for i = i + 1

		return "\n".join(to_return)

print return_with_line_numbers('sample2.txt')
	



"""
Ismail codeZ below here
"""




"""
Do you know what "script, filename = argv" does?"""
#To some extent
"""I want you to do this without using argv. Just declare the file you want in a variable:
	e.g: file_to_read = "name_of_file.txt", then keep using it.

What does "myfile = open(filename, 'r')" do? Why do you need to specify 'r'?

"""
#I've done it that way now. Plus, 'r' or 'w' show how you want
#to open the file, read or write, etc. are there other
# commands that work like that? like idk 'b' or 'c'??s
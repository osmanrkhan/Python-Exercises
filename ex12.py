#returns the words in a string in a file
import string

stringy = " THis is '' a sample' text, get me?? Cool, bro;"




def listmaker(stringthings):
	newpuncs = [i for i in string.punctuation if i != "'"]
	string_without_punc = "".join(c for c in stringthings if c not in newpuncs)

	return string_without_punc.split(" ")

print listmaker(stringy)

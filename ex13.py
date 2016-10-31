#returns the same as ex12, but now with newlines
import string

stringbean = " THis\n is \n'' a sa\nmple' text, get me?? Cool, bro;"


def breaker(coo):
	newpuncs = [i for i in string.punctuation if i != "'"]
	string_without_punc = "".join(c for c in coo if c not in newpuncs)
	return string_without_punc.split()
	
print breaker(stringbean)

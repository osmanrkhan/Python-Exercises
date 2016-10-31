#Finds the difference between two dates
import datetime
day = raw_input("Gimme a day: ")
month = raw_input("Gimme the month: ")
year = raw_input("Gimme a year: ")

if day.isdigit() and year.isdigit():
	print "All Right, here's what we have: Date: %r/%r/%r" % (month, day, year)
	date_my = datetime.date(2000, 1, 22)
	date_ur = datetime.date(int(year), int(month), int(day))
	difference = date_my - date_ur
	

	print "This is our birth-dates' difference:\n\n ", difference.days, "days \n\n"
else:
	print "Just, no. I'm leaving."
	exit()



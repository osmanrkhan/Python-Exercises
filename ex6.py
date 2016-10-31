#FInds the current time.

import datetime
 
time = datetime.datetime.now()

print "The correct date is %r/%r/%r" % (time.day, time.month, time.year)

print "The correct time is %r:%r" % (time.hour, time.minute)


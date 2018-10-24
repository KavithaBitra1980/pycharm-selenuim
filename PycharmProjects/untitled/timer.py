#Timer

#import time

from time import localtime, strftime, mktime

start_time = localtime()
print("Timer start at %s" % strftime("%X", start_time))

#Wait for user inout

input("please press enter")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print("timer stopped at %s" % strftime("%X", stop_time))
print("the wait time is %s seconds" % difference)
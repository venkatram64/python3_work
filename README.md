phthon 3 examples



python ( on CMD)

dir()

dir(__builtins__)


dir('modules')

import math

dir(math)

help(math.radians)

math.radians(180)

import math

quit()

import datetime


dir(datetime)

help(datetime.date)

gvr = datetime.date(1956, 1, 31)

#Day-name, Month-name Day-#, Year

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."

print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22,27,0)

lauch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)

print(launch_time)

print(launch_datetime)

# to get the today's date

now = datetime.datetime.today()

moon_landing = "7/20/1969"

moon_landing_datetime = datetime.datetimestrptime(moon_landing, "%m/%d/%Y")

print(moon_landing_datetime)

import random
print(dir(random))


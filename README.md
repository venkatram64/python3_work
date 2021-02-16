python 3 examples



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

https://en.wikipedia.org/wiki/URL?key=value&lif=42#History

protocal: http, https,ftp, 
host: en.wikipedia.org
port: http=80, https=443
path = wiki/URL
QueryString: key=value&lif=42
Fragment=#History


***************

step 1: pip install sqlallchemy

step 2: pip install pymysql


***************************************

To create a virtual environment:

step 1: Go to python installation
step 2: python -m venv C:\work\pwork

step 3: To activate
c:\work\pwork\Scripts\activate.bat


about dunders or magic methods
https://docs.python.org/3/reference/datamodel.html


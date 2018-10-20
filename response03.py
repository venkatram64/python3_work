from urllib import request
from urllib import parse

#print(dir(parse))  # To see the existing api methods for parse module

params = {"v":"EuC-yVzHhMI", "t": "5m56s"}
query_string = parse.urlencode(params)

print(query_string)

url = "https://www.youtube.com/watch" + "?" + query_string

response = request.urlopen(url)

print(response.isclosed())

print(response.code)

html = response.read().decode("utf-8")
print(html)

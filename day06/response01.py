from urllib import request

response = request.urlopen("https://www.wikipedia.org")

print(response.code)

"""
200: OK
400: Bad Request
403: Forbidden
404: Not Found
"""

print(response.length)

print(response.peek)

data = response.read()
print(type(data))

html = data.decode("UTF-8")
print(type(html))


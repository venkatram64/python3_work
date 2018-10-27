import json
json_file = open("movie.json","r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie)
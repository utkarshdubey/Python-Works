import urllib, json
url = "http://api.icndb.com/jokes/random"

response = urllib.urlopen(url)
data = json.loads(response.read())

print(data)
import json
import urllib.request
import webbrowser

astro_url = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY"
response = urllib.request.urlopen(astro_url)
result = json.loads(response.read())
file = open("test.txt", "w")
file.write(str(result))
file.close

webbrowser.open("test.txt")
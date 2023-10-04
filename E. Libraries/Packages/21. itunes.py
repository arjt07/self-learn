# requests package -> used to make web request
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# json.dump() -> nice Formatting
# print(json.dumps(response.json(), indent = 2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])


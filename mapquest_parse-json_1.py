import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy."
dest = "Frascati, Italy"
key = "DN0ApckU1WKQGHmVcSWLkP8NziJlD6ET" #Replace with your MapQuest key

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
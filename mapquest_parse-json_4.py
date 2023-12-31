import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "DN0ApckU1WKQGHmVcSWLkP8NziJlD6ET" 

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
         break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
         break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    json_data = requests.get(url).json()

    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    else:
        print("Error with the API. Status code:", json_status)

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
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))   
            print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")

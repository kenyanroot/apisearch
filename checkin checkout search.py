
import  json

import requests

# this code is supposed to take a users input and pass it into the payload to get ids for the specific hotels


url = "https://api.worldota.net/api/b2b/v3/search/serp/hotels/"

payload = "{\n    \"checkin\": \"2020-12-01\",\n    \"checkout\": \"2020-12-15\",\n    \"residency\": \"gb\",\n    \"language\": \"en\",\n    \"guests\": [\n        {\n            \"adults\": 2,\n            \"children\": []\n        }\n    ],\n    \"ids\": [\n        \"access_international_hotel_annex\",\n        \"rila_muam_castle_hotel\",\n        \"alama_hotel_multipurpose\",\n        \"prestige_hotel_limited\",\n        \"chimcherry_hotel_limited\",\n        \"green_suites_villa\",\n        \"kenfeli_international_palmbeach_hotel\"\n    ],\n    \"currency\": \"EUR\"\n}"

headers = {
  'Content-Type': 'application/json',
'Authorization': 'Basic MzIwODo3YmFkZGFlZi00OTIyLTRiMzUtYTczZS01NWEwYWJkYzhlMGM=',
  'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
}


response = requests.request("POST", url, headers=headers, data = payload).json()

print(response)




# passing the ids to the second apis soi can get the images and detaila ofg a specific hotel






#this code takes in the ids as parameters and uses them to bring additional details including images of the hotel


url = "https://api.worldota.net/api/b2b/v3/hotel/info/?data={\"id\":\"crowne_plaza_berlin_city_centre\",\"language\":\"en\"}"

payload = {}

headers = {
  'Content-Type': 'application/json',
'Authorization': 'Basic MzIwODo3YmFkZGFlZi00OTIyLTRiMzUtYTczZS01NWEwYWJkYzhlMGM=',
  'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
}



response = requests.request("GET", url, headers=headers, data = payload).json



#then loop over the results of the second api call
# and append them to a list which will be passed to the context of a function based view to be rendered in django.
#
# I have included the api test creds in the header so it is easier for you to understand
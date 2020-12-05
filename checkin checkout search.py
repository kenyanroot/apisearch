import json

import requests

# this code is supposed to take a users input and pass it into the payload to get ids for the specific hotels
# i have hard coded the input for testing purposes


url = "https://api.worldota.net/api/b2b/v3/search/serp/hotels/"

payload = "{\n    \"checkin\": \"2020-12-01\",\n    \"checkout\": \"2020-12-15\",\n    \"residency\": \"gb\"," \
          "\n    \"language\": \"en\",\n    \"guests\": [\n        {\n            \"adults\": 2,\n            " \
          "\"children\": []\n        }\n    ],\n    \"ids\": [\n        \"access_international_hotel_annex\"," \
          "\n        \"rila_muam_castle_hotel\",\n        \"alama_hotel_multipurpose\",\n        " \
          "\"prestige_hotel_limited\",\n        \"chimcherry_hotel_limited\",\n        \"green_suites_villa\"," \
          "\n        \"kenfeli_international_palmbeach_hotel\"\n    ],\n    \"currency\": \"EUR\"\n} "

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic <your basic auth>',
    'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
}

response = requests.request("POST", url, headers=headers, data=payload).json()

print(response['debug']['request']['ids'])

ids = response['debug']['request']['ids']


# passing the ids to the second apis soi can get the images and detaila ofg a specific hotel


# this code takes in the ids as parameters and uses them to bring additional details including images of the hotel


def multi_id_req(list_items):
    global hotels
    for item in list_items:
        hotels = {
            'id': item,
            'language': 'en',

        }
    hotels = json.dumps(hotels)
    get_url = f'https://api.worldota.net/api/b2b/v3/hotel/info/?data={hotels}'
    get_payload = {}

    get_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic MzIwODo3YmFkZGFlZi00OTIyLTRiMzUtYTczZS01NWEwYWJkYzhlMGM=',
        'Cookie': '__cfduid=d7dd143fabf3187411dfb202f1e448eb61605885792; uid=TfTb8F+35rmz7TYlB6WFAg=='
    }
    get_response = requests.request("GET", get_url, headers=get_headers, data=get_payload)
    return print(get_response.text)


multi_id_req(ids)

# then loop over the results of the second api call
# and append them to a list which will be passed to the context of a function based view to be rendered in django.

import urllib.request
from urllib.request import urlopen
import json

def places_search(a,b,c,d,e,f):
    lat = a
    lng = b
    rank = e
    key = f
    venue_type = c
    radius = d

    storage_dict = {}

    search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&rankby={}&key={}&type={}".format(lat,lng,rank,key,venue_type)

    #page 1 search
    try:
        urlData = search_url
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        #print(data)
        encoding = webURL.info().get_content_charset('utf-8')
        response = json.loads(data.decode(encoding))
        #save to venues dictionary
        #counter = 0
        for item in response['results']:
            venue = {
                'name' : item['name'],
                'type' : item['types'],
                'lat' : item['geometry']['location']['lat'],
                'long' : item['geometry']['location']['lng'],
                'id' : item['place_id']}
            storage_dict['item_{}'.format(len(storage_dict))] = venue

    except:
        pass

    #page 2 search
    try:
        urlData = search_url + "&pagetoken=" + response["next_page_token"]
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        response2 = json.loads(data.decode(encoding))
        #save to venues dictionary
        #counter = 20
        for item in response2['results']:
            venue = {
                'name' : item['name'],
                'type' : item['types'],
                'lat' : item['geometry']['location']['lat'],
                'long' : item['geometry']['location']['lng'],
                'id' : item['place_id']}
            storage_dict['item_{}'.format(len(storage_dict))] = venue

    except:
        pass

    #page 3 search
    try:
        urlData = search_url + "&pagetoken=" + response2["next_page_token"]
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        response3 = json.loads(data.decode(encoding))
        #save to venues dictionary
        #counter = 40
        for item in response3['results']:
            venue = {
                'name' : item['name'],
                'type' : item['types'],
                'lat' : item['geometry']['location']['lat'],
                'long' : item['geometry']['location']['lng'],
                'id' : item['place_id']}
            storage_dict['item_{}'.format(len(storage_dict))] = venue

    except:
        pass

    print("Search Complete. Found and saved {} venues in the venues dictionary".format(len(storage_dict)))
    return storage_dict

def test():
    print('success')

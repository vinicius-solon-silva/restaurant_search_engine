import httplib2
import json

def getGeocodeLocation(Key, inputString):

    google_api_key = Key
    locationString = inputString.replace(" ", "+")
    
    url = (f'https://maps.googleapis.com/maps/api/geocode/json?address={locationString}&key={google_api_key}')
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    return latitude,longitude
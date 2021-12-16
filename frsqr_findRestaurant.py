from google_geocode import getGeocodeLocation
import requests


def findARestaurant(mealType,location):

	geocode_key = input('Enter your google maps geocode API key: ')
	frsqr_key = input('Enter your Foursquare api key: ')

	try:
		lat, long = getGeocodeLocation(geocode_key, location)
	except IndexError:
		print("\nCant find coordinates, please enable billing on your Google Cloud.\n")
		return 0

	headers = {
        "Accept": "application/json",
        "Authorization": f"{frsqr_key}"
    }
	
	url = f"https://api.foursquare.com/v3/places/search?query={mealType}&ll={lat}%2C{long}"
	response = requests.request("GET", url, headers=headers)
	response = response.json()

	try:
		restaurant_id = response['results'][0]['fsq_id']
		restaurant_name = response['results'][0]['name']
		restaurant_address = response['results'][0]['location']['address']
	except Exception as e:
		print("\nRestaurant not found...\n")
		return 0

	photo_url = f"https://api.foursquare.com/v3/places/{restaurant_id}/photos?classifications=indoor%2Coutdoor"
	photo_response = requests.request("GET", photo_url, headers=headers)
		
	if photo_response.status_code == 200:
		photo_response = photo_response.json()
		photo_link = photo_response[0]['prefix'] + "300x300" + photo_response[0]['suffix']
	else:
		photo_link = "https://ss3.4sqi.net/img/categories_v2/arts_entertainment/themepark_120.png"

	place_dict = {
		"name": restaurant_name,
		"address": restaurant_address,
		"photo": photo_link
	}

	print("\nRestaurant name: " + place_dict['name'] + 
		  "\nAddress: " + place_dict['address'] +
		  "\nPhoto: " + place_dict['photo'] + "\n")
	

if __name__ == '__main__':

	print("\n---=== Foursquare and Google Maps Geocoding API Restaurant Search Engine ===---\n")
	mealType = input("Enter the type of meal you wish to eat: ")
	location = input("Enter the name/address of the location that you are interested in: ")
	
	findARestaurant(mealType, location)

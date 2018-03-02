import wikipedia, requests, googlemaps

from googlemaps import places


gmaps = googlemaps.Client(key='AIzaSyBN18OElCDJ6nPJvc_d-FLMZXdKVjpyTj0')


class research:

    def __init__(self):
        self.page_py = ""
        self.articles = []

    def search(self, desired_location):
        wikipedia.set_lang("fr")

        try:
            self.page_py = wikipedia.page(desired_location)

        except wikipedia.exceptions.DisambiguationError as e:
            self.articles = e.options

    def disamb(self, desired_location):
        wikipedia.set_lang("en")
        try:
            self.articles = wikipedia.search(desired_location)
        except wikipedia.exceptions.DisambiguationError as e:
            self.articles = e.options

        self.html_list = self.articles

        # for a in self.articles:
        #    self.html_list.append(a)


class map:

    def __init__(self):
        self.mapLink = ""
        self.postalAddress = ""

    def search(self, desired_location):

        # Extract information regarding the searched location
        place_info = places.places_autocomplete(gmaps, desired_location)
        # Extract google maps code
        code = (place_info[0]["place_id"])
        # Reverse geocode
        req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?place_id=' + code + '&key=AIzaSyDJROK9kvhu37rCtiJ_AmeKAPnesV0dDcI')
        print(req.json())

        # Extract postal address
        self.postalAddress = req.json()["results"][0]["formatted_address"]











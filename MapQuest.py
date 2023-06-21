import urllib.parse
import urllib.request
import json


class MapQuest:
    def __init__(self, API_key):
        self.key = API_key


    def buildURL(self, fromLocation, toLocation):
        base_url = 'http://open.mapquestapi.com/directions/v2/route'
        queryParameters = [('key', self.key), ('from', fromLocation), ('to', toLocation)]
        return base_url + '?' + urllib.parse.urlencode(queryParameters)


    def buildURL2(self, location, query, limit):
        base_url = 'http://www.mapquestapi.com/search/v4/place'
        queryParameters = [('key', self.key), ('location', location), ('q', query), ('limit', limit), ('sort', 'distance')]
        return base_url + '?' + urllib.parse.urlencode(queryParameters)


    def buildURL3(self, location):
        base_url = 'http://www.mapquestapi.com/geocoding/v1/address'
        queryParameters = [('key', self.key), ('location', location)]
        return base_url + '?' + urllib.parse.urlencode(queryParameters)


    def getResult(self, url):
        response = None
        try:
            response = urllib.request.urlopen(url)
            return json.load(response)
        finally:
            if response is not None:
                response.close()


    def totalDistance(self, locations):
        total = []
        if len(locations) > 1:
            for place in range(len(locations) - 1):
                url = self.buildURL(locations[place], locations[place + 1])
                y = self.getResult(url)
                total.append(y['route']['distance'])
            return sum(total)
        else:
            return 0


    def totalTime(self, locations):
        total = []
        if len(locations) > 1:
            for place in range(len(locations) - 1):
                url = self.buildURL(locations[place], locations[place + 1])
                y = self.getResult(url)
                total.append(y['route']['time'])
            return sum(total)
        else:
            return 0


    def directions(self, locations):
        total = ''
        if len(locations) > 1:
            for place in range(len(locations) - 1):
                url = self.buildURL(locations[place], locations[place + 1])
                y = self.getResult(url)
                for item in y['route']['legs'][0]['maneuvers']:
                    total += (item['narrative'])
                    total += '\n'
            return total
        else:
            return ''


    def getCoordinates(self, locations):
        string = ''
        url = self.buildURL3(locations)
        y = self.getResult(url)
        string += str(y['results'][0]['locations'][0]['latLng']['lng'])
        string += ', '
        string += str(y['results'][0]['locations'][0]['latLng']['lat'])
        return string


    def pointOfInterest(self, locations, keyword, results):
        list = []
        url = self.buildURL2(self.getCoordinates(locations), keyword, results)
        y = self.getResult(url)
        for result in y['results']:
            list.append(result['displayString'])
        return list

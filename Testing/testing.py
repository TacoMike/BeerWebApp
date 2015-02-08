import urllib
import urllib2

url = 'http://nodakbeerweb.appspot.com/microcontroller'

values = { "function" : "beerTemperature" ,
			'controllerID' : 'arduino_1',
          	'beerName' : 'delicious_beer_1',
          	'setTemperature' : 70,
          	'actualTemperature' : 77}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
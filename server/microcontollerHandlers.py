# Defines a bunch of handlers for requests coming from microcontrollers

# Handles a temperature request
# Should log the current temperature 
# Should respond with the desired output temperature 
def BeerTemperatureContoller(request):
	
	uID = request.request.get("controllerID")
	beerName = request.request.get("beerName")
	beerName = request.request.get("setTemperature")
	beerName = request.request.get("actualTemperature")
	return "New temperature."
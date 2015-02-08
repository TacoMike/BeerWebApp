import webapp2
import microcontollerHandlers
from google.appengine.ext import ndb

microcontrollerRequestHandlers={}
microcontrollerRequestHandlers["beerTemperature"]=microcontollerHandlers.BeerTemperatureContoller


class Index(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Congrats you got the app engine up and running! ')
        self.response.write('Crawl, walk, run haha! ')

class Microcontroller(webapp2.RequestHandler):
	def get(self):
		function = self.request.get("function")
		response = microcontrollerRequestHandlers[function](self)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(response)		


application = webapp2.WSGIApplication([
    ('/', Index),("/microcontroller", Microcontroller),
], debug=True)
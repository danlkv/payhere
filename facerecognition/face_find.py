from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import re


API_KEY = 'c50402d6847d4b8d8ac2105ed16f7f27'

app = ClarifaiApp(api_key=API_KEY)
model = app.models.get('celeb-v1.3')


class Face(ClarifaiApp):
	
	def __init__(self, source):
		url_regex = re.compile(
	        r'^(?:http|ftp)s?://' # http:// or https://
	        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	        r'localhost|' #localhost...
	        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	        r'(?::\d+)?' # optional port
	        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


		if re.match(url_regex, source) is not None:
			self.image = ClImage(url=source)
		else:
			self.image = ClImage(filename=source)

	def predict(self):

		response = model.predict([self.image])

		concepts = response['outputs'][0]['data']['regions']

		results = []

		for c in concepts:
			for e in c['data']['face']['identity']['concepts']:
				results.append({'name': e['name'], 'value': e['value'] })

		results_sorted = sorted(results, key = lambda k: int(k['value']), reverse = True)

		return results_sorted


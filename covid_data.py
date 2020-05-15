import json
import urllib.request

def load_data():
	url = 'https://covidtracking.com/api/v1/states/daily.json'
	file_name = 'covid_tmp.json'
	urllib.request.urlretrieve(url, file_name)
	raw_data = open(file_name, 'r')
	return json.load(raw_data)



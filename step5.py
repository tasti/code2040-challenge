from datetime import datetime, timedelta
import requests

TOKEN = open('token.txt', 'r').readline().rstrip('\n')

r = requests.post('http://challenge.code2040.org/api/dating', json={'token': TOKEN})
dictionary = r.json()
datestamp = dictionary['datestamp']
interval = dictionary['interval']

ISO_8601 = '%Y-%m-%dT%H:%M:%SZ'
dt = datetime.strptime(datestamp, ISO_8601)
delta = timedelta(0, interval)
dt_plus_delta = dt + delta
datestamp_plus_interval = dt_plus_delta.strftime(ISO_8601)
r = requests.post('http://challenge.code2040.org/api/dating/validate', json={'token': TOKEN, 'datestamp': datestamp_plus_interval})

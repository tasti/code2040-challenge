import requests

TOKEN = open('token.txt', 'r').readline().rstrip('\n')

r = requests.post('http://challenge.code2040.org/api/haystack', json={'token': TOKEN})
dictionary = r.json()
haystack = dictionary['haystack']
needle = dictionary['needle']

index = haystack.index(needle)
r = requests.post('http://challenge.code2040.org/api/haystack/validate', json={'token': TOKEN, 'needle': index})

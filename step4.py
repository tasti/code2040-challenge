import requests

TOKEN = open('token.txt', 'r').readline().rstrip('\n')

r = requests.post('http://challenge.code2040.org/api/prefix', json={'token': TOKEN})
dictionary = r.json()
prefix = dictionary['prefix']
array = dictionary['array']

prefix_filtered_array = filter(lambda x: not x.startswith(prefix), array)
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json={'token': TOKEN, 'array': prefix_filtered_array})

import requests

TOKEN = open('token.txt', 'r').readline().rstrip('\n')

github = 'https://github.com/tasti/code2040-challenge'
r = requests.post('http://challenge.code2040.org/api/register', json={'token': TOKEN, 'github': github})

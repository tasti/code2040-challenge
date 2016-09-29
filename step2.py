import requests

TOKEN = open('token.txt', 'r').readline().rstrip('\n')

r = requests.post('http://challenge.code2040.org/api/reverse', json={'token': TOKEN})
string = r.text

reversed_string = string[::-1]
r = requests.post('http://challenge.code2040.org/api/reverse/validate', json={'token': TOKEN, 'string': reversed_string})

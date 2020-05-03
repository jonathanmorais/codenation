import requests
import json
import sys
import string
import hashlib
from json import JSONEncoder

r  = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8b76b1b55d6bc6ca010826700d66f5acd457240b')

data = r.json()

with open('answer.json', 'w') as f:
    json.dump(data, f)

value = data['cifrado']
key = data['numero_casas']
# decrypted = data['decrifrado']

alphabet = string.ascii_lowercase

print(value)
print(key)
print("")

for c in value:
    if c in alphabet:
        position = alphabet.find(c)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        del value['cifrado']
        value += new_character
    else:
        value += c

print("")
print(value)
print("")

result = hashlib.sha1(value.encode())

print(result.hexdigest())
import requests
import json
import sys
import string
import hashlib
from json import JSONEncoder


alphabet = string.ascii_lowercase

r  = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8b76b1b55d6bc6ca010826700d66f5acd457240b')

data = r.json()

with open('answer.json', 'w') as f:
    json.dump(data, f)

value = json.dumps((data['cifrado']))
key = data['numero_casas']

decrypted_message = ""


for c in value:
    if c in alphabet:
        position = alphabet.find(c)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        decrypted_message += new_character
    else:
        decrypted_message += c

with open('answer.json', 'r+') as f:
    data = json.load(f)
    data['decifrado'] = decrypted_message
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
     
resum = hashlib.sha1(value.encode('utf-8')).hexdigest()

with open('answer.json', 'r+') as f:
    data = json.load(f)
    data['resumo_criptografico'] = resum
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()


url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=8b76b1b55d6bc6ca010826700d66f5acd457240b'

files = [
    ('answer', ('answer.json', open('answer.json', 'rb'), 'json'))
]

r = requests.post(url=url, files=files)

print(r.status_code)
print(r.content)
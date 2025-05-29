import requests
from datetime import datetime #I am using this to add a times stamp to my filee
from pprint import pprint

#My app uses the Open notify API linked below
#It does not require any API keys
# This API is being used to get a list of the astronauts in space right now and then we converted it to JSON data so python is able to read it.
endpoint = "http://api.open-notify.org/astros.json"

response = requests.get(endpoint)
data = response.json()
pprint(data)


def has_vowel(name, vowel):
    return vowel in name.lower()

astronauts = data['people']

vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = {v: 0 for v in vowels}
which_vowel = {v: [] for v in vowels}

for a in astronauts:
    name = a['name']
    name_lowercase = a ['name'].lower()
    for v in vowels:
        if has_vowel (name, v):
            count_vowels[v] += 1
            which_vowel [v].append(a ["name"])

print("\n astronauts in order of number of vowels:")

for v in vowels:
    print(f"vowel '{v.upper()}': {count_vowels[v]} astronauts")
    print("-" * 40)
    for name in which_vowel[v]:
        first_name = name.split () [0]
        sliced_name = name [:4]
        print(f"first 4 letters of '{name}'")
        print(f" {name} {first_name}, {sliced_name}")
    print('\n')



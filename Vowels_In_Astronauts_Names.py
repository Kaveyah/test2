import requests
from datetime import datetime
from pprint import pprint

endpoint = "http://api.open-notify.org/astros.json"

response = requests.get(endpoint)
data = response.json()
pprint(data)

astronauts = data['people']

vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = {v: 0 for v in vowels}
which_vowel = {v: [] for v in vowels}

for a in astronauts:
    name_lowercase = a ['name'].lower()
    for v in vowels:
        if v in name_lowercase:
            count_vowels[v] += 1
            which_vowel [v].append(a ["name"])

print("\n astronauts in order of number of vowels:")
for v in vowels:
    print(f"vowel '{v.upper()}': {count_vowels[v]} astronauts")
    print("-" * 40)
    for name in which_vowel[v]:
        first_name = name.split(" ")[0]
        print(f" {name} {first_name}")
    print('\n')
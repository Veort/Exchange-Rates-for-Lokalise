import requests


url = 'http://api.exchangeratesapi.io/v1/2010-01-15?access_key=2146e6519dc5c7836c76a433d6049c84'

response = requests.get(url)
data = response.json()

cur = ["Currency"]
exc_rat = ["Exchange rate (base EUR) as of 2010-01-15"]

for key in data['rates'].keys():
    cur.append(key)

for value in data['rates'].values():
    exc_rat.append(value)

print(cur)
print(exc_rat)
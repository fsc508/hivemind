import requests


url = 'https://twitter.com/home'

s = requests.get(url)

print(s.text)
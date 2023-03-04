import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.govtrack.us/congress/bills/#docket')

print(r)

soup = BeautifulSoup(r.content, "html.parser")
#print(soup.prettify)
s = soup.find('div')

print(soup.findAll('a'))
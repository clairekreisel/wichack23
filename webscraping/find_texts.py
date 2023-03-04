import requests
from bs4 import BeautifulSoup
import subprocess

def find_texts(location, page=0) :
    if page > 0:
        page = "?page=" + str(page);
    else:
        page = ""
    url = 'https://legiscan.com/' + location + '/legislation' + page
    print(url)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    a_elements = soup.find_all('a', class_='gaits-bill-detail')
    links = [];
    for a in a_elements:
        links.append(a.get('href'))

    return links

def main() :
    print(find_texts("US"))
    print(find_texts("NH", 2))

if __name__ == "__main__" : main()
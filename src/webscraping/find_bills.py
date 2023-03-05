"""
This file is for finding the bill texts from legiscan.
For Claire, Avery, and Rosaline's WicHacks 2023 Project

this file written primarily by Avery Carle

copyleft under GNU GPL 3.0 License
"""

import requests
from bs4 import BeautifulSoup
import re
import time



"""
Scans the legiscan page for a location and returns a list of links to texts

Parameters:
    location: String of the two letters of the state to scan (US for federal and DC for Washington D.C.)
    page: 0-indexed value of which page of the bills to scan (0 by default)

Returns: a list of the links to bill texts from that page

note: some pages are blank for some reason, not sure why
"""
def find_bills(location, page=0) :
    if page > 0:
        page = "/?&page=" + str(page);
    else:
        page = ""
    url = 'https://openstates.org/' + location.lower() +'/bills' + '/' + page
    #print(url)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    return __get_links(soup)

"""
Helper function for parsing site into the list of links

Parameters:
    soup: a BeautifulSoup object for a legiscan legislation page

Returns: a list of the links to bill texts from that page
"""
def __get_links(soup):
    a_tags = soup.find_all('a', class_='td-link')
    links = [];
    for a in a_tags:
        rex = re.compile("bill")
        if (rex.search(a.get('href'))) :
            links.append("https://openstates.org" + a.get('href'))
        #time.sleep(0.25)
    return links



def main() :
    #print(find_bills("US"))
    print(find_bills("NH"))
   

if __name__ == "__main__" : main()
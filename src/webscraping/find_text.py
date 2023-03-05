"""
This file is for finding the bill texts from legiscan.
For Claire, Avery, and Rosaline's WicHacks 2023 Project

this file written primarily by Avery Carle

copyleft under GNU GPL 3.0 License
"""

import requests
from bs4 import BeautifulSoup



"""
Scans the legiscan page for a location and returns a list of links to texts

Parameters:
    location: String of the two letters of the state to scan (US for federal and DC for Washington D.C.)
    page: 0-indexed value of which page of the bills to scan (0 by default)

Returns: a list of the links to bill texts from that page

note: some pages are blank for some reason, not sure why
"""
def find_texts(location, page=0) :
    if page > 0:
        page = "?page=" + str(page);
    else:
        page = ""
    url = 'https://legiscan.com/' + location + '/legislation' + page
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
    a_elements = soup.find_all('a', class_='gaits-bill-detail')
    links = [];
    for a in a_elements:
        links.append("https://legiscan.com/" + a.get('href'))

    return links

# def find_all_texts(location) :
#     url = 'https://legiscan.com/' + location + '/legislation'
#     r = requests.get(url);
#     soup = BeautifulSoup(r.content, "html.parser")
#     links = __get_links(soup);
#     page = 1
#     page_options = soup.find_all('li',  class_='pager-item')
#     last_page_option = page_options[len(page_options) - 1]
#     while (last_page_option.content != 47) :
#         print(len(links))
#         links = links + find_texts(location, page)
#         page_options = soup.find_all('li',  class_='pager-item')
#         last_page_option = page_options[len(page_options) - 1]
#         page += 1

#     return links


def main() :
    print(find_texts("US"))
    print(find_texts("NH", 2))
    # print(find_all_texts("US"))

if __name__ == "__main__" : main()
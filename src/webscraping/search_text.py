"""
This file is for searching a text for keywords.
For Claire, Avery, and Rosaline's WicHacks 2023 Project

this file written primarily by Avery Carle

copyleft under GNU GPL 3.0 License
"""

import requests
from bs4 import BeautifulSoup
from find_bills import find_bills
from pdfminer.high_level import extract_text
import os
import re
import urllib



def get_text(url) :
    text = None
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    a_tags = soup.find_all('a')

    reASPX = re.compile('Format=pdf')
    reDirect = re.compile('.pdf')
    for a in a_tags:
        
        a_link = a.get('href')
        if re.search(reASPX, str(a_link)) or re.search(reDirect, str(a_link)) :
            return __extract_pdf(str(a_link))
    


    
    
    
def __extract_html(link) :
    pass

def __extract_pdf(link) :
    urllib.request.urlretrieve(link, "temp.pdf")
    text = extract_text("temp.pdf")
    os.remove("temp.pdf")
    return text
    

        

def main() :
    urls = find_bills("TN")
    
    print(urls[5])
    print(get_text(urls[5]))
    

if __name__ == "__main__" : main()
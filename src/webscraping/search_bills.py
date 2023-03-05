"""
This file is for searching a text for keywords.
For Claire, Avery, and Rosaline's WicHacks 2023 Project

this file written primarily by Avery Carle

copyleft under GNU GPL 3.0 License
"""

from find_bills import find_bills
from search_text import search_text

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"]

"""
searches all 50 states and scans their bills
"""
def search_bills() :
    matched_bills = {}
    for state in STATES :
        bills = find_bills(state)
        for bill in bills:
            matches = search_text(bill)
            print(matches, bill)
            matched_bills[bill] = (state, matches)
    return matched_bills

def main() :
    print(search_bills())

if __name__ == "__main__" : main()

        
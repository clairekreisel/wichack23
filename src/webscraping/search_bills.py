
from find_bills import find_bills
from search_text import __get_text, search_text

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"]

def search_bills() :
    matched_bills = {}
    for state in STATES :
        bills = find_bills(state)
        for bill in bills:
            matches = search_text(bill)
            #print(matches, state)
            matched_bills[bill] = (state, matches)
    return matched_bills

def main() :
    print(search_bills())

if __name__ == "__main__" : main()

        

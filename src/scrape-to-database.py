from sys import path as syspath
from os import path as ospath
syspath.append(ospath.dirname(ospath.abspath(__file__))+'/database')
syspath.append(ospath.dirname(ospath.abspath(__file__))+'/webscraping')
from search_bills import search_bills
from sqlConnect import sqlConnector

bills = search_bills()
conn = sqlConnect.sqlConnector()

for bill in bills.keys():
    state = bills[bill][0]
    reasons = bills[bill][1]
    conn.addBill(state, bill, reasons)

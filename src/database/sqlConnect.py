import mysql.connector
from mysql.connector import Error
import pandas
from stateDict import location_dict

#None of this works if this is run in multiple places
#DO NOT RUN IN MULTIPLE PLACES

class sqlConnect:    
    def __init__(self):
        connection = None
        try: #TODO: figure out host connection
            connection = mysql.connector.connect(host="localhost" ,user="dbUsr" ,passwd="not a password, very secure", database="wittyDBname")
        except Error:
            print(f"Error: '{Error}'"
        self.connection = connection

    def get_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall() #returns tuple of tuples (tuple 1 = row, tuple 2 = value)
        
    def post_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()

    def addBill(self, location, pdf_link, *reasons):
            lid = location_dict[location]
            bid = (int)(get_query("SELECT max(bid) FROM blc")[0][0]) + 1
            post_query(f"INSERT INTO blc VALUES ({bid}, {lid})")
            post_query(f"INSERT INTO blt VALUES ({bid}, {pdf_link})")
            lSum = (int)(get_query(f"SELECT sum FROM lst WHERE lid={lid}")[0][0]) + 1
            post_query(f"UPDATE SET sum={lSum} WHERE lid={lid}")

    def getBills(self, location):
        bidL = get_query(f"SELECT bid FROM blc WHERE lid={location_dict[location]}")
        billLinkL = []
        for bid in bidL:
            billLinkL.append(get_query(f"SELECT link FROM blt WHERE bid={bid}"))
        return billLinkL

    def getSum(self, location):
        return (int)(get_query(f"SELECT sum FROM lst WHERE lid={location_dict[location]}")[0][0])
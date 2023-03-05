import mysql.connector
from mysql.connector import Error

from stateDict import location_dict

#None of this works if this is run in multiple places
#DO NOT RUN IN MULTIPLE PLACES

class sqlConnector:    
    def __init__(self):
        connection = None
        try: #TODO: figure out remote host connection
            connection = mysql.connector.connect(host="localhost" ,user="dbUsr" ,passwd="not a password, very secure", database="wittyDBName")
        except Error:
            raise
        print(connection)
        self.connection = connection

    def get_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall() #returns tuple of tuples (tuple 1 = row, tuple 2 = value)
        except:
            return 0
        
    def post_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except:
            pass

    def addBill(self, location, pdf_link, *reasons):
        lid = location_dict[location]
        bid = (self.get_query("SELECT max(bid) FROM blc"))[0][0]
        if(bid is None):
            bid = 0
        else:
            bid = int(bid) + 1
        print(bid)
        self.post_query(f"INSERT INTO blc VALUES ({bid}, {lid})")
        print("blc insert")
        self.post_query(f"INSERT INTO blt VALUES ({bid}, '{pdf_link}')")
        print("blt insert")
        lSum = int((self.get_query(f"SELECT sum FROM lst WHERE lid={lid}")[0][0])) + 1
        self.post_query(f"UPDATE lst SET sum={lSum} WHERE lid={lid}")
        

    def getBills(self, location):
        bidL = self.get_query(f"SELECT bid FROM blc WHERE lid={location_dict[location]}")
        billLinkL = []
        for bid in bidL:
            billLinkL.append(self.get_query(f"SELECT link FROM blt WHERE bid={bid}"))
        return billLinkL

    def getSum(self, location):
        return (int)(self.get_query(f"SELECT sum FROM lst WHERE lid={location_dict[location]}")[0][0])

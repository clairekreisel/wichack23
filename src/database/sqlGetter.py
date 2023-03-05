import mysql.connector
from mysql.connector import Error

from stateDict import location_dict

#SAFE TO RUN IN MULTIPLE PLACES

class sqlGetter:    
    def __init__(self):
        connection = None
        try: 
            connection = mysql.connector.connect(host="localhost" ,user="dbUsr" ,passwd="not a password, very secure", database="wittyDBName")
        except Error:
            raise
        print(connection)
        self.connection = connection

    def get_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall() #returns list of tuples (list = row, tuple 2 = value)
        except:
            return 0

    def getBills(self, location):
        bidL = self.get_query(f"SELECT bid FROM blc WHERE lid={location_dict[location]}")
        billLinkL = []
        for bid in bidL:
            billLinkL.append(self.get_query(f"SELECT link FROM blt WHERE bid={bid}"))
        return billLinkL

    def getSum(self, location):
        return (int)(self.get_query(f"SELECT sum FROM lst WHERE lid={location_dict[location]}")[0][0])

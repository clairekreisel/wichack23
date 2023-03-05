from sqlConnect import sqlConnector

conn = sqlConnector()

conn.addBill("Montana", "test")

#conn.post_query("INSERT INTO blt VALUES (0, 'test')")

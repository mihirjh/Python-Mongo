from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://localhost:27017")
db=client.MihirDB
# Issue the serverStatus command and print the results
resultset = db.inventory.find( {'status': 'D' })
print("Resultset Values:")
print(resultset)

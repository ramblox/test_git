import pymongo
client = pymongo.MongoClient("mongodb+srv://Bharath123:permitted@cluster0.mmb7b.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name" : "Bharath",
   "email" : "rambharath2445@gmail.com",
   "surname" : "Ram"}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
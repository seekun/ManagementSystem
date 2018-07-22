import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["paper"]
mycol = mydb["articles"]

mydict = {}

def updatedb(old_col, new_col):

    mydb.collection.update(old_col, new_col)
    print('11111')
    mycol.update_one(old_col, new_col)
    print("success")



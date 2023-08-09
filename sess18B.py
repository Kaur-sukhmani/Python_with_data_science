import pymongo
import certifi  # pip install certifi | if SSL error
from tabulate import tabulate

ca = certifi.where()


class MongoDBHelper:

    def __init__(self, collection='customer'):
        uri = "mongodb+srv://root:root123@cluster0.yoemesb.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri, tlsCAFile=ca)
        self.db = client['gwpds']
        self.collection = self.db[collection]

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document inserted:", result)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document deleted ", result)

    def fetch(self, query=""):
        documents = self.collection.find(query)
        # if len(query)!=0:
        #     documents = self.collection.find_one(query)
        #     documents =
        # else:
        #     documents = self.collection.find(query)
        # for document in documents:
            # print(document)
        # print(tabulate(documents, headers="keys", tablefmt="grid"))
        return list(documents)

    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)

# authentication
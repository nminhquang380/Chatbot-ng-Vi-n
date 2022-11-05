import pymongo
import numpy as np

myclient = pymongo.MongoClient("localhost:27017")

mydb = myclient['local']

mycol = mydb['myCollection']

#print(mycol.find_one())


def find_ans(ques, topic):
    query = mycol.find_one({"label" : topic, "question" : ques})
    return query

def retrieve_vector_document(vector):
    document = mycol.find_one({"vector": vector})
    res = {
        "id": str(document["_id"]),
        "label": document["label"],
        "question": document["question"],
        "answer": document["answer"],
        "link": document["link"],
    }
    return res

matrix = [np.array(doc["vector"]) for doc in mycol.find({"vector" : {"$exists" : True}}, {"vector" : 1})] 

if __name__ == "__main__":
    print()
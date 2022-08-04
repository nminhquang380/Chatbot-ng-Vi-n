import pymongo


myclient = pymongo.MongoClient("localhost:27017")

mydb = myclient['local']

mycol = mydb['myCollection']

#print(mycol.find_one())


def find_ans(ques, topic):
    query = mycol.find_one({"label" : topic, "question" : ques})
    return query



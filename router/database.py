# import motor.motor_asyncio


# #connect to the database
# MONGO_DETAILS = "mongodb://localhost:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.local

# collection = database.get_collection("myCollection")

from bson.objectid import ObjectId
import pymongo


myclient = pymongo.MongoClient("localhost:27017")

database = myclient['local']

collection = database['myCollection']




#query the document
def document_query(document) -> dict:
    return {
        "id": document["_id"],
        "label": document["label"],
        "question": document["question"],
        "answer": document["answer"],
        "link": document["link"],
    }

#retrieve a document with a matching ID
def retrieve_document(id: str) -> dict:
    document = collection.find_one({"_id": ObjectId(id)})
    if document:
        return document
    

#retrive all documents in the database
def retrieve_documents():
    documents = []
    for document in collection.find():
        documents.append(document_query(document))
    return documents

#add a new document into to the database
def add_document(document_data: dict) -> dict:
    document = collection.insert_one(document_data)
    new_document = collection.find_one({"_id" : document.inserted_id})
    return document_query(new_document)

#update a document iwht a matching ID
def update_document(id: str, data: dict):
    if len(data) < 1:
        return False
    document = collection.find_one({"_id": ObjectId(id)})
    if document:
        updated_document = collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_document:
            return True
        return False

#delete a student student from the database
def delete_document(id: str):
    document = collection.find_one({"_id" : ObjectId(id)})
    if document:
        collection.delete_one({"_id" : ObjectId(id)})
        return True
    return False


# if __name__ == "__main__":
#    document = retrieve_document("61f1191a9f25a48832112d46")
#    print(document)
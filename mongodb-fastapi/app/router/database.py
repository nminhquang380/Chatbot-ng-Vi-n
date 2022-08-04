from bson.objectid import ObjectId
import motor.motor_asyncio


#connect to the database
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.local

collection = database.get_collection("myCollection")

#query the document
def document_query(document) -> dict:
    return {
        "id": document["_id"],
        "label": document["label"],
        "question": document["question"],
        "answer": document["answer"],
        "link": document["link"],
    }

#retrive all documents in the database
async def retrieve_documents():
    documents = []
    async for document in collection.find():
        documents.append(document_query(document))
    return documents

#add a new document into to the database
async def add_document(document_data: dict) -> dict:
    document = await collection.insert_one(document_data)
    new_document = await collection.find_one({"_id" : document.inserted_id})
    return document_query(new_document)

#retrieve a document with a matching ID
async def retrieve_document(id: str) -> dict:
    document = await collection.find_one({"_id": ObjectId(id)})
    if document:
        return document_query(document)
    
#update a document iwht a matching ID
async def update_document(id: str, data: dict):
    if len(data) < 1:
        return False
    document = await collection.find_one({"_id": ObjectId(id)})
    if document:
        updated_document = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_document:
            return True
        return False

#delete a student student from the database
async def delete_document(id: str):
    document = await collection.find_one({"_id" : ObjectId(id)})
    if document:
        await collection.delete_one({"_id" : ObjectId(id)})
        return True
    return False

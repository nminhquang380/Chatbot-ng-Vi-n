from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

#import built module
from router.database import (
    add_document,
    delete_document,
    retrieve_document,
    retrieve_documents,
    update_document
)

from router.models.documents import (
    ErrorResponseModel,
    ResponseModel,
    DocumentSchema,
    UpdateDocumentSchema,
)


router = APIRouter()

#retrieve document with ID
@router.get("/{id}", response_description="document data retrieved")
async def get_document_data(id):
    # document = await retrieve_document(id)
    document = retrieve_document(id)
    return document
    # if document:
    #     return ResponseModel(document, "document data retrieved successfully")
    # return ErrorResponseModel("An error occurred.", 404, "document doesn't exist.")


#add document
@router.post("/", response_description="Documents Added")
async def add_document_data(document : DocumentSchema =  Body(...)):
    document = jsonable_encoder(document)
    new_document = await add_document(document)
    return ResponseModel(new_document, "Document added successfully.")

#retrieve all documents
@router.get("/", response_description="Documents retrieved")
async def get_documents():
    # documents = await retrieve_documents()
    documents = retrieve_documents()
    if documents:
        return ResponseModel(documents, "documents data retrieved successfully")
    return ResponseModel(documents, "Empty list returned")

#update document with ID
@router.put("/{id}")
async def update_document_data(id: str, req: UpdateDocumentSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_document = await update_document(id, req)
    if updated_document:
        return ResponseModel(
            "document with ID: {} name update is successful".format(id),
            "document name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the document data.",
    )

#delete document with ID
@router.delete("/{id}", response_description="document data deleted from the database")
async def delete_document_data(id: str):
    deleted_document = await delete_document(id)
    if deleted_document:
        return ResponseModel(
            "document with ID: {} removed".format(id), "document deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "document with id {0} doesn't exist".format(id)
    )
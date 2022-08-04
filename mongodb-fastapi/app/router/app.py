from fastapi import FastAPI

from app.router.routes.document import router as DocumentRouter

app = FastAPI()

app.include_router(DocumentRouter, tags=["Document"], prefix="/Document")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
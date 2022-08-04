import uvicorn
from fastapi import FastAPI
from router.routes.document import router as DocumentRouter
from responser.routes.answer import router as AnswerRouter
#from responser.response_question import response

app = FastAPI()

app.include_router(DocumentRouter, tags=["Thay đổi dữ liệu"], prefix="/document")
app.include_router(AnswerRouter, tags=["Hỏi đáp Đảng viên"], prefix="/answer")

# @app.get("/hoidap", tags=["Hỏi Đáp Đảng Viên"])
# async def hoi_dap(message):
#     answer = response(message)
#     return {"câu trả lời ": answer}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port= 8000, reload=True)
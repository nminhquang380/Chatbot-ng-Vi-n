from fastapi import APIRouter

#import buildt module
from responser.response_question import response

router = APIRouter()

#find the answer
@router.get("/hoidap",response_description="Question answered")
async def hoi_dap(message):
    answer = response(message)
    return {"answer": answer}
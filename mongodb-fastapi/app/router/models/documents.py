from typing import Optional
from pydantic import BaseModel, Field

class DocumentSchema(BaseModel):
    label: str = Field(...)
    question: str = Field(...)
    answer: str = Field(...)
    link: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "label": "thutuc",
                "question": "quy định kết nạp đảng viên trong trường hợp đảng viên là người có đạo ? ",
                "answer": "Quy chế của Đảng trong việc kết nạp Đảng viên không yêu cầu tôn giáo",
                "link": "https://luatvietnam.vn/luat-su-tu-van/nguoi-theo-dao-thien-chua-co-duoc-ket-nap-dang-khong-142643-faqs.html",
            }
        }

class UpdateDocumentSchema(BaseModel):
    label: Optional[str]
    question: Optional[str]
    answer: Optional[str]
    link: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "label": "thutuc",
                "question": "quy định kết nạp đảng viên trong trường hợp đảng viên là người có đạo ? ",
                "answer": "Quy chế của Đảng trong việc kết nạp Đảng viên không yêu cầu tôn giáo",
                "link": "https://luatvietnam.vn/luat-su-tu-van/nguoi-theo-dao-thien-chua-co-duoc-ket-nap-dang-khong-142643-faqs.html",
            }
        }
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
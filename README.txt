# Bài toán đặt ra:
    Xây dựng một chatbot trả lời câu hỏi của đảng viên.

# Luồng hoạt động:
https://drive.google.com/file/d/1iqf87udOLGS7lseVLDVErkCnpu-t0RX5/view?usp=sharing

# Mô tả sản phẩm:
- Một bộ API gồm:
 + API trả lời câu hỏi của đảng viên.
 + API CRUD dữ liệu (cụ thể là kịch bản trả lời câu hỏi) trong Database.

1. Cài đặt môi trường và các thư viện cần thiết.
1.1. Tạo môi trường ảo Venv
    a. Windows
    python -m venv venv
    venv/Scripts/activate
    b. Ubuntu
    python -m venv \venv
    source venv/bin/activate
1.2. Cài đặt thư viện cần thiết
    pip install -r requirements.txt


2. Cách chạy hệ thống
    python main.py

# Chưa biết setup Database.
    - Ở đây sử dụng MongoDB.
    - Với tập dữ liệu chứa trong Collection ở local.
    - Một document gồm một kịch bản trả lời câu hỏi:
     + '_id' : id của kịch bản.
     + 'label' : Nhãn của câu hỏi.
     + 'question' : Câu hỏi.
     + 'answer' : Câu trả lời.
     + 'link' : Đường link tài liệu tham khảo.
     + 'vector' : Một mảng (Array) được tạo ra từ việc nhúng (Embedding) câu hỏi.


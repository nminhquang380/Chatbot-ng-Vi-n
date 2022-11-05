# DỰ ÁN CHATBOT TRẢ LỜI CÂU HỎI CỦA ĐẢNG VIÊN

## Mô tả

Đây là một dự án dành cho đối tượng Đảng viên. Giúp giải đáp một số thắc mắc thường gặp của Đảng viên về điều lệ Đảng và một số thủ tục.
 
## Cách cài đặt

### Cài đặt môi trường và các thư viện cần thiết.

**Bước 1: Tạo môi trường ảo Venv**

*1. Windows*

    python -m venv venv
    venv/Scripts/activate

*2. Linux (Ubuntu)*

    python -m venv \venv
    source venv/bin/activate

**Bước 2: Cài đặt thư viện cần thiết**

    pip install -r requirements.txt

**_Lưu ý:_**

Do module FastText có thể gặp lỗi khi sử dụng phương pháp install pip hay pip3 của Python, nên ở đây chúng tôi khuyến khích bạn đọc tài liệu hướng dẫn install của chính FastText tại https://fasttext.cc/docs/en/supervised-tutorial.html.

### *Huẩn luyện cho mô hình FastText. (Tùy chọn)*

Trong module thêm tệp dữ liệu cho việc huấn luyện, có tên là “train_data_final.txt”. Về format của dữ liệu, bạn có thể tham khảo chính file “train_data_final.txt” của chúng tôi. Sau đó bạn chạy file “model_fasttext.py”, hệ thống sẽ tự sinh một model “model_dangvien.bin”, hoặc bạn có thể sử dụng luôn model chúng tôi đã train cùng tên. 

### Cách chạy hệ thống

    python main.py

## Setup Database

- Ở đây sử dụng MongoDB.
- Với tập dữ liệu chứa trong Collection ở local.
- Một document gồm một kịch bản trả lời câu hỏi:
     + '_id' : id của kịch bản.
     + 'label' : Nhãn của câu hỏi.
     + 'question' : Câu hỏi.
     + 'answer' : Câu trả lời.
     + 'link' : Đường link tài liệu tham khảo.
     + 'vector' : Một mảng (Array) được tạo ra từ việc nhúng (Embedding) câu hỏi.

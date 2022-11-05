from responser import (
    find_answer_db,
    find_answer_gg,
    classify_question,
    similarity_search,
)

from router import database

# def test(ques = ""):
#     ques = ''
#     while True:
#         #nhap cau hoi tu ban phim
#         ques = input('Mời bạn nhập câu hỏi:\n')
#         if ques == 'no':
#             break

#         #normalize cau hoi theo dung format, su dung model de predict topic cua cau hoi
#         ques = classify_question.nomalize(ques)
#         label = classify_question.predict_topic(ques)

#         if find_answer_db.find_ans(ques, label):
#             ans = find_answer_db.find_ans(ques,label)
#             print(ans['answer'])
#             print(ans['link'])

#         else:
#             print("Dưới đây là một số link tham khảo cho câu hỏi trên. Bạn đọc có thể tìm đọc:\n")
#             find_answer_gg.googlesearch(ques)

#tra loi cau hoi dc nhap
def response(message):

    #chuan hoa cau hoi
    ques = classify_question.nomalize(message)

    #phan loai topic
    label = classify_question.predict_topic(message)

    #tim kiem cau hoi trong db
    document = find_answer_db.find_ans(ques, label)
    if document:
        res = document['answer'] + "\n Đây là link bạn có thể tham khảo: " + document['link']
        return res

    k, vector = similarity_search.find_similar(ques)
    if k >= 0.65:
        document = find_answer_db.retrieve_vector_document(vector.tolist())
        answer = "dưới đây là câu trả lời cho câu hỏi tương tự:\n"+ document["answer"] + "\n" + document["link"] + "\nMức độ sát nghĩa: {}".format(k)
        document["question"] = ques
        if k >= 0.75:
            new_document = database.add_document(document)
        return  answer


    #tim kiem cau hoi tren gg (neu khong ton tai cau tra loi tren db)
    
    return find_answer_gg.googlesearch(message)


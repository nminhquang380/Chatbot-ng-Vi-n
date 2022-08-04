from responser import (
    find_answer_db,
    find_answer_gg,
    classify_question
)

def test(ques = ""):
    ques = ''
    while True:
        #nhap cau hoi tu ban phim
        ques = input('Mời bạn nhập câu hỏi:\n')
        if ques == 'no':
            break

        #normalize cau hoi theo dung format, su dung model de predict topic cua cau hoi
        ques = classify_question.nomalize(ques)
        label = classify_question.predict_topic(ques)

        if find_answer_db.find_ans(ques, label):
            ans = find_answer_db.find_ans(ques,label)
            print(ans['answer'])
            print(ans['link'])

        else:
            print("Dưới đây là một số link tham khảo cho câu hỏi trên. Bạn đọc có thể tìm đọc:\n")
            find_answer_gg.googlesearch(ques)

#tra loi cau hoi dc nhap
def response(message):

    #chuan hoa cau hoi
    ques = classify_question.nomalize(message)

    #phan loai topic
    label = classify_question.predict_topic(message)

    #tim kiem cau hoi trong db
    if find_answer_db.find_ans(ques, label):
        return  find_answer_db.find_ans(ques, label)['answer']

    #tim kiem cau hoi tren gg (neu khong ton tai cau tra loi tren db)
    
    return find_answer_gg.googlesearch(message)


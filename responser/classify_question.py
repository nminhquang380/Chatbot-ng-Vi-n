import fasttext

model = fasttext.load_model("responser\\model_dangvien.bin")

def nomalize(s):
    #convert to lower case
    s = s.lower()
    n = len(s)
    i = 0
    #add space to punctuation
    while i < n:
        if s[i] in '?.!,':
            stemp = s[:i] + ' ' + s[i] + ' ' + s[i+1:]
            i += 1
            n += 2
            s = stemp
        i += 1
    return s

def predict_topic(s):
    #predict input topic
    return(model.predict(s)[0][0][9:])

if __name__ == "__main__":
    while(True):
        ques = input(">>")
        nomalize(ques)
        if ques == "exit":
            break
        print(ques)
        topic = predict_topic(ques)
        print(topic)
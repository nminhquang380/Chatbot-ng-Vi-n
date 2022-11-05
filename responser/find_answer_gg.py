try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


# to search

def googlesearch(query):
    lst = "Dưới đây là một số link tham khảo cho câu hỏi trên. Bạn đọc có thể tìm đọc:\n"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        lst += j
    return lst

print(googlesearch("nhiem vu cua dang vien la"))
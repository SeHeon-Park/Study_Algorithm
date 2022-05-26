def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return True
    return False

def solution(phone_book):
    phone_book.sort(key=lambda x: x)
    print(phone_book)
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) == phone_book[i+1]:
            continue
        if not check(phone_book[i], phone_book[i+1]):
            return False
    return True

# 문자열의 sort는 알파벳 정렬이다! (예 'ABC' < 'AD') ('123' < '13') 중요!!


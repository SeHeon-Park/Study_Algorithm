## 문자열 정렬로 풀이
def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    for i in range(l-1):
        for j in range(i+1, l):
            if phone_book[i][0] != phone_book[j][0] or len(phone_book[i]) >= len(phone_book[j]):
                break
            if phone_book[i] in phone_book[j]:
                return False
    return True


## 해시로 풀이
def solution(phone_book):
    dic = {}
    for number in phone_book:
        dic[number] = len(number)
    for number in phone_book:
        temp = ''
        for n in number:
            temp += n
            if temp in dic.keys() and temp != number:
                return False
    return True

# 문자열의 sort는 알파벳 정렬이다! (예 'ABC' < 'AD') ('123' < '13') 중요!!


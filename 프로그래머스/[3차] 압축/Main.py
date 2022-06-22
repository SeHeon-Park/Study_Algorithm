def get_alpha():
    dic = {}
    alpha = 'A'
    for i in range(1, 27):
        dic[alpha] = i
        alpha = chr(ord(alpha)+1)
    return dic

def solution(msg):
    dic = get_alpha()
    answer = []
    start, end, number = 0, 1, 27
    word = ''
    while True:
        print(word)
        if end == len(msg)+1:
            break
        word = msg[start:end]
        if word in dic.keys():  # key중에 word가 있는지 확인
            end += 1
            temp = word
        else:
            answer.append(dic[temp])
            dic[word] = number
            number += 1
            start = end-1
            end = start+1
        
    answer.append(dic[temp])
    return answer
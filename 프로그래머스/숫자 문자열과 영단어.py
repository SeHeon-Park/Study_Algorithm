def solution(s):
    answer = ""
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    temp = ""
    for word in s:
        if word.isalpha():
            temp += word
        else:
            answer += str(word)
        if temp in dic.keys():
            answer += dic[temp]
            temp = ""
    print(answer)
    return answer

def solution(enroll, referral, seller, amount):
    answer = {}
    answer["BOSS"] = 0
    for e in enroll:
        answer[e] = 0
    dic = {}
    for i in range(len(referral)):
        if referral[i] == '-':
            dic[enroll[i]] = "BOSS"
        else:
            dic[enroll[i]] = referral[i]

    def recursion(cur, price):
        if price < 10 or cur == "BOSS":
            answer[cur] = answer[cur] + price
            return
        ten = price//10
        answer[cur] = answer[cur] + price-ten
        recursion(dic[cur], ten)
        return

    for s, a in zip(seller, amount):
        recursion(s, a*100)
    ans = []
    for e in enroll:
        ans.append(answer[e])
    return ans

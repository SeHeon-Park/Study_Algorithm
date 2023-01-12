def solution(numbers):
    answer = []
    scope = {1, 3, 7, 15, 31}

    def make_binary(n):
        s = ""
        while True:
            if n == 0:
                break
            r = n%2
            n = n//2
            s = str(r) + s
        return s

    def check(s):
        l = len(s)
        for i in range(l//2+1):
            if s[i] == '1' and (l-i-1) in scope:
                if check_divide(s[i+1:]) and check_divide("0"*(l-2*i-1)+s[:i]):
                    return True
        return False

    def check_divide(s):
        if len(s) == 1 and s[0] == '1':
            return True
        if s.count('1') == 0 and len(s) in scope:
            return True
        if s.count('1') == 0 and len(s) not in scope:
            return False
        if s[len(s)//2] == '1':
            if check_divide(s[:len(s)//2]) and check_divide(s[len(s)//2+1:]):
                return True
        return False

    for n in numbers:
        if n == 1:
            answer.append(1)
            continue
        if check(make_binary(n)):
            answer.append(1)
        else:
            answer.append(0)
    return answer
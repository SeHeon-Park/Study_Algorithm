def gcd(w, h):
    for i in range(min(w, h), 0, -1):
        if w%i==0 and h%i==0:
            return i

def solution(w,h):
    g = gcd(w, h)
    answer = w*h-int((w/g+h/g-1)*g)
    return answer

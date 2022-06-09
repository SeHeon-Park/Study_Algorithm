def inter_union(s1, s2):
    inter, union = [], [] # 교집합, 합집합
    for i in s1:
        for j in s2:
            if i == j:
                inter.append(i)
                s2.remove(j)
                break
        union.append(i)
    for i in s2:
        union.append(i)
    return inter, union

def solution(str1, str2):
    str1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]  # isalpha: 알파벳인지 확인
    str2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    if len(str1) > len(str2):
        inter, union = inter_union(str1, str2)
    else:
        inter, union = inter_union(str1, str2)
    if len(inter) == 0:
        return 0
    return int((len(inter)/len(union)) * 65536)

## 아스키코드 통해서 문자 판별
# 대문자: 65~90
# 소문자: 97~122
# 숫자: 48~57

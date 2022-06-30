def solution(skill, skill_trees):
    answer = 0
    dic = {}
    level = 1
    for s in skill:
        dic[s] = level
        level += 1
    
    for k in skill_trees:
        level, flag = 1, 0
        for s in k:
            if s in dic.keys():
                if dic[s] != level:
                    flag = 1
                    break
                level +=1
        if flag == 0:
            answer += 1
    

    return answer
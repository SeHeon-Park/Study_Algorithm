import re
import math

def get_fee(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]
    
def get_time(i, o, fees):
    i_time = re.split(":", i)
    o_time = re.split(":", o)
    minute = (int(o_time[0])-int(i_time[0])) * 60 + (int(o_time[1]) - int(i_time[1]))
    return minute
    
def solution(fees, records):
    dic = {}
    car, answer = [], []
    for r in records:
        info = re.split(" ", r)
        if info[2] == "OUT":
            time = get_time(dic[info[1]][0], info[0], fees)
            dic[info[1]][2] = dic[info[1]][2] + time
            dic[info[1]][1] = "OUT"
        else:
            if info[1] in dic.keys():
                dic[info[1]][0] = info[0]
                dic[info[1]][1] = "IN"
            else:
                dic[info[1]] = [info[0], info[2], 0]
    for i in dic.items():
        if i[1][1] == "IN":
            time = get_time(i[1][0], "23:59", fees)
            dic[i[0]][2] = i[1][2] + time
        car.append([i[0], get_fee(dic[i[0]][2], fees)])
    car.sort(key=lambda x : x[0])
    for c in car:
        answer.append(c[1])
    return answer
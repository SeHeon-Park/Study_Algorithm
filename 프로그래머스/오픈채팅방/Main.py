def solution(record):
    command = []
    answer = []
    dic = {}
    for r in record:
        t = r.split(" ")
        for s in range(len(t)):
            if t[0] == "Enter" or t[0] == "Change":
                dic[t[1]] = t[2]
        if t[0] == "Enter" or t[0] == "Leave":
            command.append([t[0], t[1]])
    for c in command:
        if c[0] == "Enter":
            answer.append(dic[c[1]] + "님이 들어왔습니다.")
        else:
            answer.append(dic[c[1]] + "님이 나갔습니다.")

    return answer
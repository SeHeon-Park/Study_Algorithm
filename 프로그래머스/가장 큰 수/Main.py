def solution(numbers):
    temp_list = []
    numbers_str = [str(num) for num in numbers]
    for n in numbers_str:
        temp = n
        temp += temp * 2
        temp_list.append([n, temp])
    answer = ''
    temp_list.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(temp_list)):
        answer += temp_list[i][0]
    return str(int(answer))
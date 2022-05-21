def recursive(numbers, curr, target, answer):
    if len(numbers) == 0:
        if curr == target: answer.append(1)
        return
    recursive(numbers[1:], curr+numbers[0], target, answer)
    recursive(numbers[1:], curr-numbers[0], target, answer)
    return len(answer)

def solution(numbers, target):
    answer = recursive(numbers, 0, target, [])
    return answer

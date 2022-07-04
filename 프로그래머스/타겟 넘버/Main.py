def recursive(numbers, target, s, answer):
    if not numbers:
        if s == target:
            answer += 1
        return answer
    answer = recursive(numbers[:-1], target, s+numbers[-1], answer)
    answer = recursive(numbers[:-1], target, s-numbers[-1], answer)
    return answer

def solution(numbers, target):
    return recursive(numbers, target, 0, 0)
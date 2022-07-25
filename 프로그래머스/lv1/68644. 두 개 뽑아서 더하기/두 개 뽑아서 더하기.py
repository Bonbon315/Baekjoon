def solution(numbers):
    answer = []
    for j in range(0, len(numbers)):
        for i in range(0, len(numbers)):
            if i != j:
                answer.append(numbers[j] + numbers[i])
    
    removedup = set(answer)
    answer = list(removedup)
    answer.sort()
    return answer
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        one = numbers[i]
        for j in range(i+1, len(numbers)):
            two = numbers[j]
            answer.append(one + two)
    
    
    return sorted(list(set(answer)))
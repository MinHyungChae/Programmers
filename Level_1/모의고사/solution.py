from itertools import cycle

def solution(answers):
    answer = []
    cycles = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    
    count = [0, 0, 0]
    
    for a in answers:
        for i in range(0, 3):
            if a == next(cycles[i]):
                count[i] += 1
    
    maximum = max(count)
    
    for i, value in enumerate(count):
        if value == maximum:
            answer.append(i+1)
    return sorted(answer)

# 같은 로직을 iter()를 사용해서 풀었을 때, 런타임 에러가 발생했다. 이유는 모르겠다 ㅜㅜ

def solution(prices):
    answer = []
    for i in range(len(prices)):
        target = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if target > prices[j]:
                break
        answer.append(count)
    
    
    return answer
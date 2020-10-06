def solution(n):
    total = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in total:
            total -= set(range(2*i, n+1, i))
    
    return len(total)
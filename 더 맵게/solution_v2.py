import heapq

def solution(scov, K):
    answer = 0
    heapq.heapify(scov)
    
    if scov[0] >= K:
        return 0
    
    count = 0
    while len(scov) > 1:
        if scov[0] >= K:
            return count
        else:
            first = heapq.heappop(scov)
            second = heapq.heappop(scov)
            new = first + second*2
            
            heapq.heappush(scov, new)
            count += 1
    if scov[0] >= K:
        return count
    return -1
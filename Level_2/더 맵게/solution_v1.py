# 정확성: 52.4
# 효율성: 0.0
# 합계: 52.4 / 100.0

import collections

def solution(scov, K):
    answer = 0
    if min(scov) >= K:
        return 0
    
    count = 0
    while scov: 
        scov = collections.deque(sorted(list(set(scov))))
        if scov[0] >= K:
            return count
        else:
            first = scov.popleft()
            second = scov.popleft()
            new = first + (second*2)
            
            scov.append(new)
            count += 1
    return -1
# 정확성: 33.3
# 합계: 33.3 / 100.0

import itertools

def solution(number, k):
    answer = []
    # number에서 k개의 수를 제거했을 때 가장 큰 수 return
    num_len = [i for i in range(len(number))]
    rmv_idx = list(itertools.combinations(num_len, k))
    
    
    for rmv in rmv_idx:
        list_number = list(number)
        for r in rmv:
            list_number[r] = ''

        toString = ''.join(list_number)
        answer.append(int(toString))
    
    return str(max(answer))
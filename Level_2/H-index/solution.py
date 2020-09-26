# 정렬
# 100점  ㅎㅎㅎ

def solution(citations):
    answer = []
    citations.sort()
    
    if citations[0] == citations[-1]:
        return citations[0]
    elif len(citations) <= citations[0]:
        return len(citations)
    else:
        for i in range(citations[0], citations[-1] + 1):
            u_count = 0
            d_count = 0
            for c in citations:
                if c >= i:
                    u_count += 1
                elif c <= i:
                    d_count += 1
            if (u_count >= i) and (d_count <= i):
                answer.append(i)
            
        return max(answer)
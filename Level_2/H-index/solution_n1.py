# 정렬
# 81.3

def solution(citations):
    citations.sort()
    possible = []
    # x 이상이 x개, 나머지는 x 미만일 때 x 구하기.
    for i in range(citations[0], citations[-1]+1):
        a_list = []
        b_list = []
        for c in citations:
            if c >= i:
                a_list.append(c)
            else:
                b_list.append(c)
        if len(a_list) == i:
            possible.append(i)
    
    answer = sorted(possible, reverse = True)
    return answer[0]
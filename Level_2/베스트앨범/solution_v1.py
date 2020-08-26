# 정확성 20.0
# 합계 : 20.0 / 100.0

def solution(genres, plays):
    answer = []
    # sort 우선순위 : 장르 -> 재생 수 -> 고유번호 오름차순 
    plays_w_index = list(zip(plays, [i for i in range(0, len(plays))]))
    # print(plays_w_index)
    overall = list(zip(genres, plays_w_index))
    # print(overall)
    
    order = {}
    for o in overall:
        if o[0] not in order:
            order[o[0]] = o[1][0]
        else:
            order[o[0]] += o[1][0]
    
    # genre 우선순위
    # order = sorted(order, key = lambda v : order[v])
    sorted_order = sorted(order, key = lambda o : o[1], reverse = True)
    print(sorted_order)
    
    for so in sorted_order:
        temp = []
        for o in overall:
            if o[0] == so:
                temp.append(o[1])
        temp_answer = sorted(temp, key = lambda t: (t[0], -t[1]),reverse = True)
        
        if len(temp_answer) > 2:
            answer.append(temp_answer[0][1])
            answer.append(temp_answer[1][1])
        else:
            for t in temp_answer:
                answer.append(t[1])
            
    return answer
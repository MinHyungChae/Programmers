def solution(priorities, location):
    answer = []
    idx_p = []
    for i in range(len(priorities)):
        idx_p.append([priorities[i], i])
        
    while idx_p:
        check = idx_p.pop(0)
        flag = 0
        for p in idx_p:
            if p[0] > check[0]:
                flag = 1
            # 큰 거 발견한 경우
        if flag == 1:
            idx_p.append(check)
        else:
            # 큰거 없었음
            answer.append(check)
            
    print(answer)
    for i in range(len(answer)):
        if answer[i][1] == location:
            return i+1
# 완전탐색

def solution(brown, yellow):
    answer = []
    # m >= n
    # 1) m+n = brwon//2 + 2
    # 2) (m-2)*(n-2) = yellow
    # yellow의 약수를 구한다. -> 각각 +2 해서 m, n 의 조합을 구함. 2)번에 의함.
    y_list = []
    for i in range(1, (yellow//2)+2):
        if yellow % i == 0:
            x = i
            y = yellow // i
            if (x<y):
                y_list.append([y+2, x+2])
            else:
                y_list.append([x+2, y+2])
    
    b = brown//2 + 2
    # 1) 번에 의해서 m과 n 의 합의 조건을 알 수 있음.
    for mn in y_list:
        if mn[0] + mn[1] == b:
            return [mn[0], mn[1]]

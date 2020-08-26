# 정확성 : 100.0
# 합계 : 100.0 / 100.0

def solution(clothes):
    # 의상 종류별로 dictionary 만든다
    group = {}
    answer = 1
    
    for cloth in clothes:
        if cloth[1] not in group:
            # 만약 아직 추가되지 않은 종류라면
            group[cloth[1]] = 1
        else:
            group[cloth[1]] += 1
            # 만약 이미 추가된 종류라면, 해당 종류의 가짓수를 + 1 해준다

    # 각 그룹의 가짓수 + 1 한 만큼(옷을 입지 않는 경우도 경우의 수에 포함되므로)한 값끼리 곱해준다.
    for i in group.values():
        answer *= (i+1)
    answer -= 1
    # 전체 경우에서 아무것도 입지 않는 경우를 한가지 빼준다.
    return answer
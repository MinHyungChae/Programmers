import math

def makeGroup(str):
    result = []
    for i in range(len(str) - 1):
        target = str[i:i+2].strip()
        if len(target) == 2 and target.isalpha() == True:
            result.append(target.lower())
    return result

def solution(str1, str2):
    answer = 0
    jcd = 0
    group_1 = makeGroup(str1)
    group_2 = makeGroup(str2)

    set_group_1 = list(set(group_1))
    set_group_2 = list(set(group_2))
    
    inter = list(set(group_1) & set(group_2))
    union = list(set(group_1) | set(group_2))
    
    inter_result = []
    union_result = []
    # 교집합 만큼 만들기
    for target in inter:
        count = min(group_1.count(target), group_2.count(target))
        temp = [target for i in range(count)]
        inter_result.extend(temp)
    
    # 합집합 만큼 만들기
    for target in union:
        count = max(group_1.count(target), group_2.count(target))
        temp = [target for i in range(count)]
        union_result.extend(temp)
    
    print(inter_result)
    print(union_result)
    if len(inter_result) == 0 and len(union_result) == 0 :
        jcd = 1
    else:
        jcd = len(inter_result) / len(union_result)
    
    return math.floor(jcd*65536)
            
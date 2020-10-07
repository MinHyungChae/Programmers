import re

def solution(dartResult):
    answer = 0
    r = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = r.findall(dartResult)
    result = []
    
    for idx, score in enumerate(scores):
        point = score[0]
        bonus = score[1]
        option = score[2]
        
        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3
        
        if option == '*':
            if idx == 0:
                result.append(int(point)**bonus*2)
            else:
                result[-1] *= 2
                result.append(int(point)**bonus*2)
        elif option == '#':
            result.append(int(point)**bonus*-1)
        else:
            result.append(int(point)**bonus)
            
    return sum(result)
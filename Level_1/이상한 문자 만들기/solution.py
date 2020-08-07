def solution(s):
    answer = ''
    flag = 0 # 해당 알파벳의 짝/홀수 index 여부 판별
    for alpha in s :
        # 해당 index 가 공백일 경우 flag = 0 으로 짝수번째로 reset
        if alpha == ' ' :
            flag = 0
            answer += (' ')
            continue
        else :
            # 해당 index 가 짝수일 때 대문자로 변경
            if flag == 0 :
                answer += (alpha.upper())
                flag = 1
            else : 
                # 해당 index 가 홀수일 때 소문자로 변경
                answer += (alpha.lower())
                flag = 0
                
    return answer
def solution(s):
    s_list = list(s)
    answer = sorted(s_list, key = lambda x: ord(x), reverse = True)
    
    return ''.join(answer)
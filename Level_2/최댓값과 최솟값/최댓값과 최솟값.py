def solution(s):
    answer = ''
    s_list = list(map(int, s.split()))
    minn = min(s_list)
    maxx = max(s_list)
    
    return str(minn) + ' ' + str(maxx)
def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        # 홀수
        idx = len(s)//2
        return s[idx]
    else:
        idx = len(s)//2
        return s[idx-1 : idx+1]
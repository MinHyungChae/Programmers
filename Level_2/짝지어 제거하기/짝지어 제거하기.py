from collections import deque

def solution(s):
    if len(s) == 1:
        return 0
    
    s_q = deque(s)
    answer = []
    
    while s_q:
        if len(answer) > 0:
            if answer[-1] == s_q[0]:
                answer.pop()
                s_q.popleft()
            else:
                answer.append(s_q.popleft())
        else:
            answer.append(s_q.popleft())
            
    if len(answer) != 0:
        return 0
    else:
        return 1
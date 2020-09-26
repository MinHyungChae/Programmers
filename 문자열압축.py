import collections

def solution(s):
    answer = []
    rotate = len(s)//2
    
    if len(s) == 1:
        return 1
    
    for r in range(1, rotate +1):
        temp_answer = ''
        s_list = [s[i * r:(i + 1) * r] for i in range((len(s) + r - 1) // r )]
        s_list = collections.deque(s_list)
        
        while s_list:
            check = s_list.popleft()
            count = 1
            while s_list:
                if s_list[0] == check:
                    count += 1
                    s_list.popleft()
                else:
                    break
            if count == 1:
                temp_answer += check
            else:
                temp_answer += str(count)
                temp_answer += check
        
        answer.append(len(temp_answer))
    
    return sorted(answer)[0]
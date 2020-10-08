def solution(s):
    answer = []
    
    s = s[2:-2]
    s = s.split("},{")
    
    s.sort(key = len)
    for si in s:
        si_list = si.split(',')
        
        for num in si_list:
            if int(num) not in answer:
                answer.append(int(num))
        
    
    
    return answer
def solution(s):
    answer = []
    if len(s) == 1:
        return s.upper()
    
    s_list = s.split(' ')
    for word in s_list:
        answer.append(word.capitalize())
    return ' '.join(answer)
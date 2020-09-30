def solution(s):
    answer = True
    if s[0] != '(' or s[-1] != ')':
        return False
    
    left_count = 0
    right_count = 0
    for idx in s:
        if idx == '(':
            left_count += 1
        else:
            right_count += 1
            if right_count > left_count:
                return False
    if left_count == right_count:
        return True
    else:
        return False
def solution(n):
    n_list = list(str(n))
    n_list = sorted(n_list, reverse = True)
    
    return int(''.join(n_list))
    
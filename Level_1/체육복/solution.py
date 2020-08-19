def solution(n, lost, reserve):
    answer = 0
    # if duplicate in lost and reserve, can't lend
    # remove duplicate -> use 'set'!
    count = 0
    lost.sort()
    reserve.sort()
    
    remainder = set(reserve) - set(lost)
    remainder = list(remainder)
    
    need = set(lost) - set(reserve)
    need = list(need)
    
    for r in remainder:
        front = r-1
        back = r+1
        if front in need:
            need.remove(front)
        elif back in need:
            need.remove(back)
    
    answer = n - len(need)
    return answer
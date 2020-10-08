def solution(nums):    
    set_num = set(nums)
    set_count = len(set_num)
    
    avail_count = len(nums)//2
    
    if set_count <= avail_count:
        return set_count
    else:
        return avail_count
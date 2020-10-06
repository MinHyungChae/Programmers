def solution(arr):
    mini = min(arr)
    arr.remove(mini)
    
    if len(arr) == 0:
        return [-1]
    
    return arr
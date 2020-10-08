import collections
def solution(arr):
    answer = []
    arr = collections.deque(arr)
    
    while arr:
        first = arr.popleft()
        answer.append(first) 
        while arr:
            if arr[0] == first:
                arr.popleft()
            else:
                break
    return answer
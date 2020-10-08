import collections
def getGCD(x, y):
    while y:
        x, y = y, x%y
    return x

def getLCM(x, y):
    return x*y // getGCD(x, y)

def solution(arr):
    arr_q = collections.deque(arr)
    while len(arr_q) > 1:
        x = arr_q.popleft()
        y = arr_q.popleft()
        z = getLCM(x, y)
        arr_q.append(z)
    return arr_q[0]
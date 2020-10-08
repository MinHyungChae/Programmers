def getFib(num):
    f_list = [0, 1, 1]
    if num <= 2:
        return f_list[num]
    else:
        for i in range(3, num+1):
            f_list.append(f_list[i-1] + f_list[i-2])
    return f_list[-1]

def solution(n):
    return getFib(n)%1234567
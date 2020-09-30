import itertools

def solution(nums):
    comb = list(itertools.combinations(nums, 3))
    count = 0
    for com in comb:
        s_com = sum(com)
        flag = 0
        for i in range(2, (s_com // 2) + 1):
            if s_com % i == 0:
                flag = 1
                break
        if flag == 0:
            count += 1

    return count
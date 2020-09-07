# 완전 탐색
import itertools

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    com_list = []
    
    # 전체 요소들 간의 순열 구하기
    for i in range(1, len(num_list)+1):
        comb = list(map(''.join, itertools.permutations(num_list, i)))
        com_list.extend(comb)

    # 전체 요소를 integer 로 변환
    com_list = list(map(int, com_list))
    # 전체 요소에서 중복 제거
    com_list = list(set(com_list))
    
    # 소수 검증 후 소수면 +1
    for c in com_list:  
        if(check(int(c))) == True:
            answer += 1
            print(c)
    
    return answer

# 소수 검증 함수
def check(n):
    if (n<2):
        return False
    for i in range(2, n):
        if(n%i == 0):
            return False
    return True
# 참고 풀이

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))

# str 의 비교시 ascii 코드로 비교함. 앞자리부터 순서대로 아스키로 비교하기 때문에 가능한 코드

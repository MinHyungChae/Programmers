# 정확성 69.2
# 효율성 0.0
# 합계 69.2 / 100.0

# phone_book 리스트를 길이 순으로 정렬하고
# 첫번째 부터 순차적으로 자신 다음에 있는 요소들에서 자신을 포함한 경우 return False 하고 break 건다

def solution(phone_book):
    answer = True
    # 문자열의 길이 순으로 배열 정렬
    phone_book.sort(key = len)
    
    for i in range(0, len(phone_book)):
        for j in range(i+1, len(phone_book)):
            keyword = str(phone_book[i])
            if (keyword in phone_book[j]):
                answer = False
                break
    return answer
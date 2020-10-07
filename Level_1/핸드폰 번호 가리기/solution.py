def solution(phone_number):
    len_phone = len(phone_number)
    left = '*'*(len_phone - 4)
    right = phone_number[-4:]
    
    return left + right
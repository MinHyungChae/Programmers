# 정렬
# 27.3점

def solution(numbers):
    answer = ''
    # 제일 첫 자리로 일단 먼저 정렬
    # 같은 숫자로 시작하면 큰 순서로 정렬. 단, 마지막 자리가 0이면 최소값으로 침
    first_dict = dict()
    for num in numbers:
        if str(num)[0] not in first_dict:
            first_dict[str(num)[0]] = [num]
        else:
            first_dict[str(num)[0]].append(num)
    
    for d in first_dict:
        d_list = first_dict[d]
        # print(d_list)
        a_list = []
        b_list = []
        for d_in in d_list:
            if d_in % 10 != 0:
                a_list.append(d_in)
            else:
                b_list.append(d_in)
        a_list = sorted(a_list, reverse = True)
        b_list = sorted(b_list, reverse = True)
        a = ''.join(map(str, a_list))
        b = ''.join(map(str, b_list))
        first_dict[d] = a+b
        
    #print(first_dict)
    final_dict = sorted(first_dict.items(), reverse = True)
    #print(final_dict)
    
    for f in final_dict:
        answer += f[1]
    return answer
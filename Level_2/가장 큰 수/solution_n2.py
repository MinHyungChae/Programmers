# 정렬
# 36.4

import itertools
def solution(numbers):
    answer = ''
    dict_numbers = dict()
    for num in numbers: 
        if str(num)[0] not in dict_numbers:
            dict_numbers[str(num)[0]] = [str(num)]
        else:
            dict_numbers[str(num)[0]].append(str(num))
    #print(dict_numbers)
    
    final_list = []
    for dic in dict_numbers:
        dic_list = dict_numbers[dic]
        final_list.append([int(dic), (getBest(dic_list))])
    
    final_list = sorted(final_list, key = lambda x : -x[0])
    for f in final_list:
        answer += f[1]
            
    return answer

def getBest(input):
    if len(input) != 1:
        iter_list = list(itertools.permutations(input, len(input)))
        str_list = [''.join(v) for v in iter_list]
        return sorted(str_list)[-1]
    else:
        return input[0]
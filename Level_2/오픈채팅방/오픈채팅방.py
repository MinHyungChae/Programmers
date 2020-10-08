def solution(record):
    answer = []
    id_dic = {}
    for r in record:
        r_list = r.split(' ')
        if r_list[0] == "Enter":
            id_dic[r_list[1]] = [r_list[2]]
        elif r_list[0] == "Change":
            id_dic[r_list[1]].append(r_list[2])
                
    for r in record:
        r_list = r.split(' ')
        name = id_dic[r_list[1]][-1]
        if r_list[0] == "Enter":
            answer.append(name+"님이 들어왔습니다.")
        elif r_list[0] == "Leave":
            answer.append(name+"님이 나갔습니다.")
    
    return answer
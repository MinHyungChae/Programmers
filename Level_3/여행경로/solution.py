def solution(tickets):
    answer = []
    dict_ticket = dict()
    for ticket in tickets:
        if ticket[0] not in dict_ticket:
            dict_ticket[ticket[0]] = [ticket[1]]
        else:
            dict_ticket[ticket[0]].append(ticket[1])
            
    for i in dict_ticket.keys():
        dict_ticket[i].sort(reverse = True)
    
    print(dict_ticket)
    start = ['ICN']
    
    while start:
        top = start[-1]
        if top not in dict_ticket or len(dict_ticket[top]) == 0:
            answer.append(start.pop())
        else:
            start.append(dict_ticket[top][-1])
            dict_ticket[top].pop()
    answer.reverse()
    return answer
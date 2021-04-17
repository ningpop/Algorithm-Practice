def solution(participant, completion):
    answer = ''
    comp_dic = {}
    
    for part in participant:
        if part not in comp_dic:
            comp_dic[part] = 1
        else:
            comp_dic[part] += 1
    
    for comp in completion:
        if comp not in comp_dic:
            comp_dic[comp] = 1
        else:
            comp_dic[comp] -= 1
            
    for key, value in comp_dic.items():
        if value > 0:
            answer = key
    return answer
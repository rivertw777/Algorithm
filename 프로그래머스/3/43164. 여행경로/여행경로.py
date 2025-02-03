def solution(tickets):
    d = {}
    for i in tickets:
        if i[0] not in d:
            d[i[0]] = [i[1]]
        else:
            d[i[0]].append(i[1])
            
    for i in d:
        d[i].sort()
    
    print(d)
    print()
            
    st = ["ICN"]
    answer = []
    while st:
        start = st[-1]
        
        if start in d and d[start]:
            
            item = d[start].pop(0)
            st.append(item)
            
            print(st, " - ", d)
            if len(st) == len(tickets) + 1:
                return st
            
        else:
            answer.append(st.pop())
                        
    return answer[::-1]
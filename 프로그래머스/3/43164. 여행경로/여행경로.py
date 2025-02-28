def solution(tickets):
    dct = {}
    
    for t in tickets:
        if t[0] not in dct:
            dct[t[0]] = []
            dct[t[0]].append(t[1])
        else:
            dct[t[0]].append(t[1])
            
    for i in dct:
        dct[i].sort()
        
    st = ["ICN"]
    ans = []
    while st:
        start =  st[-1]
        
        if start in dct and dct[start]:
            st.append(dct[start].pop(0))
        else:
            ans.append(st.pop())
                        
    return ans[::-1]

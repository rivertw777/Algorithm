def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    
    # k가 남아있다면 뒤에서부터 k개를 제거
    if k > 0:
        st = st[:-k]
        
    return ''.join(st)

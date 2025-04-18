n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input())

result = []
for a in range(n-7):
    for b in range(m-7):
        w_cnt = 0 
        b_cnt = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 짝수인 경우
                    if graph[i][j] != 'W': 
                        w_cnt += 1
                    else: 
                        b_cnt += 1 
                else: # 홀수인 경우
                    if graph[i][j] != 'W': 
                        b_cnt += 1 
                    else:
                        w_cnt += 1 
        
        result.append(w_cnt)
        result.append(b_cnt)                
        
print(min(result))
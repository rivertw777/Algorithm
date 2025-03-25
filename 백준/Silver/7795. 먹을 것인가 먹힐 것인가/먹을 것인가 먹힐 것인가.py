t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    b.sort(reverse=True)
        
    cnt = 0
    index = 0
    for i in range(n):        
        while index < m and a[i] <= b[index]:
            index += 1
        
        cnt += m - index
                                  
    print(cnt)
k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

start = 1
end = sum(line) // n 

result = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in line:
        cnt += i // mid
        
    if cnt >= n:  # 개수가 너무 많이 나오면 숫자를 높임
        start = mid + 1
        result = mid
    elif cnt < n:  # 개수가 적으면 숫자를 낮춤
        end = mid - 1

print(result)
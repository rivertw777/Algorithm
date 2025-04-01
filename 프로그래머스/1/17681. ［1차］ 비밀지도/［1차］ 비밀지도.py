def to_binary_list(arr, n):
    
    result = []
    for number in arr:
        temp = ""
        while number > 0:
            temp += str(number % 2)
            number //= 2
        
        prefix = ""
        for i in range(n - len(temp)):
            prefix += "0"
                
        result.append(prefix + temp[::-1])
        
    return result
    
def solution(n, arr1, arr2):
    first = to_binary_list(arr1, n)
    second = to_binary_list(arr2, n)

    answer = []
    for i in range(n):
        temp = ""        
        for j in range(n):
            if first[i][j] == "1" or second[i][j]  == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    
    return answer
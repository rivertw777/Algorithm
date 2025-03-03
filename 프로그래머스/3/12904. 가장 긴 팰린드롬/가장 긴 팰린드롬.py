def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1  # 팰린드롬의 길이 반환

def solution(s):    
    max_length = 1
    
    for i in range(len(s)):
        # 홀수 길이의 팰린드롬
        len1 = expand_around_center(s, i, i)
        # 짝수 길이의 팰린드롬
        len2 = expand_around_center(s, i, i + 1)
        max_length = max(max_length, len1, len2)
    
    return max_length

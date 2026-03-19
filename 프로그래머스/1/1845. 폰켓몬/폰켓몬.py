def solution(nums):
    unique_count = len(set(nums))
    pick = len(nums) // 2
    return min(unique_count, pick)
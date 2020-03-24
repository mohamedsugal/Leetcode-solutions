from typing import List

nums = [9,6,4,2,3,5,7,0,1]

# Sorting   Time: O(nlogn)  Space: O(1)
def missingNumberSorting(nums: List[int]) -> int:
    nums.sort()
    if nums[-1] != len(nums):
        return len(nums)
    elif nums[0] != 0:
        return 0
    for i in range(1, len(nums)): 
        expected_num = nums[i-1] + 1 
        if nums[i] != expected_num: 
            return expected_num

# Hashset   Time: O(n)  Space: O(n)
def missingNumberHashSet(nums: List[int]) -> int:
    nums_set = set(nums)
    for number in range(len(nums) + 1): 
        if number not in nums_set: 
            return number

# XOR       Time: O(n)  Space: O(1)
def missingNumberXOR(nums: List[int]) -> int: 
    missing = len(nums)
    for i, num in enumerate(nums): 
        missing ^= i ^ num
    return missing

print(missingNumberXOR(nums))
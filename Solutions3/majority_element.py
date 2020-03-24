from typing import List 

def majorityElement(nums: List[int]) -> int:
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num
    

nums = [1,2,3,3]
print(majorityElement(nums))

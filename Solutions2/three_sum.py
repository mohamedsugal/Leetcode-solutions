from typing import List 

def three_sum(nums: List[int]) -> List[List[int]]: 
    nums.sort()
    result = set()
    for i in range(len(nums) - 2): # (-2) can't pass left & right
        left, right = i + 1, len(nums) - 1
        while left < right: 
            current_sum = nums[i] + nums[left] + nums[right]        
            if current_sum < 0: 
                left += 1
            elif current_sum > 0: 
                right -= 1
            else:
                if current_sum == 0: 
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
    return list(result)

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
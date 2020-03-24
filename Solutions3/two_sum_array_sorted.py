from typing import List 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # note that index starts at 1 
        left, right = 0, len(numbers)-1
        while left < right: 
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target: 
                return [left+1, right+1]
            elif curr_sum < target: 
                left += 1 
            else: 
                right -= 1

numbers = [2,7,11,15]
target = 9
t = Solution()
print(t.twoSum(numbers, target))
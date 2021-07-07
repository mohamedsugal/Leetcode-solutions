from typing import List 
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        arr = self.nums[:]
        for i in range(len(self.nums)): 
            swap_idx = random.randrange(i, len(self.nums))
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
        return arr

nums = [3, 1, 2]
obj = Solution(nums)
print(obj.reset())
print(obj.shuffle())
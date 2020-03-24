from typing import List

class Solution:
    # Time complexity: O(n)     Space complexity: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table, result = {}, []
        for num in nums: 
            hash_table[num] = 1
        for num in range(1, len(nums)+1): 
            if num not in hash_table: 
                result.append(num)
        return result
    
    # Time Complexity: O(n)     Space complexity: O(1)
    def findDisappearedNumber(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): 
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0: 
                nums[new_index] *= -1
        print(nums)

        result = []
        for i in range(1, len(nums)+1): 
            if nums[i-1] > 0: 
                result.append(i)
        print(result)


nums = [4,3,2,7,8,2,3,1]
test = Solution()
test.findDisappearedNumber(nums)

        
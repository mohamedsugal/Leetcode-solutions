from typing import List 
import collections

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elements, stack = {}, []
        for i in range(len(nums2)): 
            while stack and nums2[i] > stack[-1]: 
                elements[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        res = []
        for i in nums1: 
            if i in elements: 
                res.append(elements[i])
            else: 
                res.append(-1)
        print(res)



# nums1 = [1,3,5,2,4]
# nums2 = [6,5,4,3,2,1,7]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
t = Solution()
print(t.nextGreaterElement(nums1, nums2))
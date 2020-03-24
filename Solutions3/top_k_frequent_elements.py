from typing import List 
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        bucket = collections.defaultdict(list)
        
        for key,val in frequency.items(): 
            bucket[val].append(key)
        
        res = []
        count = len(nums)
        while len(res) < k: 
            if bucket[count]: 
                res += bucket[count]
            count -= 1
        
        return res[:k]
        
nums = [1,1,1,2,2,2,3,3,3,4,4,4,4]
k = 2
t = Solution()
print(t.topKFrequent(nums, k))

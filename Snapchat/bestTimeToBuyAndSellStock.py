from typing import List 
import unittest 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window approach => Time: O(n) Space: O(1)
        left, right = 0, 1 
        profit = 0 
        while right < len(prices):
            if prices[right] < prices[left]: 
                left = right 
                right += 1
            else: 
                profit = max(profit, prices[right] - prices[left])
                right += 1
        return profit


class TestSolution(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 5)
    def test2(self): 
        self.assertEqual(Solution().maxProfit([2,1,2,1,0,1,2]), 2)

if __name__ == "__main__": 
    unittest.main()
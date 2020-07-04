from typing import List


class Solution:
    # Brute force   Time: O(n^2)    Space: O(1)
    @staticmethod
    def most_water(height: List[int]) -> int:
        max_area = float('-inf')
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                min_val = min(height[i], height[j])
                max_area = max(max_area, min_val * (j - i))
        return max_area

    # Two pointers  Time: O(n)      Space: O(1)
    @staticmethod
    def most_water2(height: List[int]) -> int:
        max_area = float('-inf')
        left, right = 0, len(height) - 1
        while left < right:
            min_val = min(height[left], height[right])
            max_area = max(max_area, min_val * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.most_water2(heights))

from typing import List

'''
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
from typing import List
'''


# TODO: 1239. Maximum Length of a Concatenated String with Unique Characters
class Solution:
    def max_length(self, arr: List[str]) -> int:
        unique = ['']
        max_len = 0
        for char in arr:
            for c in unique:
                temp = c + char
                if self.is_unique(temp):
                    unique.append(temp)
                    max_len = max(max_len, len(temp))
        return max_len

    @staticmethod
    def is_unique(temp: str) -> bool:
        return len(set(temp)) == len(temp)


# test = ["un", "iq", "ue"]
test = ["cha", "r", "act", "ers"]
# test = ["abcdefghijklmnopqrstuvwxyz"]
# test = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
s = Solution()
print(s.max_length(test))

# TODO: 1246. Palindrome Removal
# Given an integer array arr, in one move you can select a
# palindromic subarray arr[i], arr[i+1], ..., arr[j]
# where i <= j, and remove that subarray from the given array.
# Note that after removing a subarray, the elements on the left and on
# the right of that subarray move to fill the gap left by the removal.
# Return the minimum number of moves needed to remove all numbers from the array.
'''
Example 1:
Input: arr = [1,2]
Output: 2

Example 2:
Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
'''

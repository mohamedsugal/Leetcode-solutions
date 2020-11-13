from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict()
        left = right = length = 0

        while right < len(s):
            if s[right] in window:
                del window[s[left]]
                left += 1
            else:
                window[s[right]] = 1
                right += 1
                length = max(length, right - left)

        return length


def test_solution():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3


test_solution()

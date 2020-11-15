from collections import defaultdict


class Solution:
    @staticmethod
    def longest_substring(s: str) -> int:
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


ret1 = Solution.longest_substring("abcabcbb")
ret2 = Solution.longest_substring("bbbbb")
ret3 = Solution.longest_substring("pwwkew")
print(ret1)
print(ret2)
print(ret3)

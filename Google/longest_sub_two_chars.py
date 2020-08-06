from collections import Counter
import unittest


class Solution:
    @staticmethod
    def longest_substring_with_two_chars(s: str) -> int:
        window = Counter()
        max_len = start = 0
        for end, c in enumerate(s):
            window[c] += 1
            while len(window) > 2:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len


class TestSolution(unittest.TestCase):
    def test_inputs(self):
        self.assertAlmostEqual(Solution.longest_substring_with_two_chars("eceba"), 3)
        self.assertAlmostEqual(Solution.longest_substring_with_two_chars("ccaabbb"), 5)





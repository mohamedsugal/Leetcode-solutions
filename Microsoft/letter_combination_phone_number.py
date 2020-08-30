from typing import List


class Solution:
    @staticmethod
    def letter_combinations(digits: str) -> List[str]:
        combinations = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i']}
        for i in range(len(combinations[digits[0]])):
            for j in range(len(digits)):
                print(i, j)


digit = "23"
s = Solution()
s.letter_combinations(digit)

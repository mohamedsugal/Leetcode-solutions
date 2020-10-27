from typing import List
from collections import deque


class Solution:
    @staticmethod
    def letter_combinations(digits: str) -> List[str]:
        mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = deque([''])
        for d in digits:
            for _ in range(len(combinations)):
                prev = combinations.popleft()
                for letter in mapping[int(d)]:
                    combinations.append(prev + letter)
        return [*combinations] if digits else ''


s = Solution()
print(s.letter_combinations('345'))
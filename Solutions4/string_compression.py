from typing import List


class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        res = []
        count, index = 1, 0
        for curr in range(1, len(chars)+1):
            prev = curr - 1
            if curr < len(chars) and chars[prev] == chars[curr]:
                count += 1
            else:
                chars[index] = chars[prev]
                index += 1
                if count > 1:
                    for n in str(count):
                        chars[index] = n
                        index += 1
                count = 1
        chars = chars[:index]
        print(chars)
        return index


string = ["a", "a", "b", "b", "c", "c", "c"]
solution = Solution()
print(solution.compress(string))

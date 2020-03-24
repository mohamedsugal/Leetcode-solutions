class Solution:
    @staticmethod
    def jewels_and_stones(jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
            continue
        return count


J = "z"
S = "ZZ"
solution = Solution()
print(solution.jewels_and_stones(J, S))

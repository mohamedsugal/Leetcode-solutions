class Solution:
    @staticmethod
    def fib(N: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)


N = 3
solution = Solution()
print(solution.fib(N))

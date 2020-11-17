class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        if len(s) < 1:
            return 0
        index, sign, result = 0, 1, 0
        while index < len(s)-1 and s[index] == " ":
            index += 1
        if s[index] in "-+":
            sign = 1 if s[index] == "+" else -1
            index += 1
        while index < len(s) and s[index].isdigit():
            result = 10 * result + int(s[index])
            index += 1
        return max(-2**31, min(result * sign, 2**31-1))


def test_solution():
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -2147483648
    assert solution.myAtoi("91283472332") == 2147483647

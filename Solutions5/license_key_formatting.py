class Solution:
    @staticmethod
    def license_key_formatting(S: str, K: int) -> str:
        count, i = 0, len(S) - 1
        result = []
        while i >= 0:
            curr = S[i].upper()
            if curr == "-":
                i -= 1
            elif count != 0 and count % K == 0:
                result.insert(0, "-")
                count = 0
            else:
                result.insert(0, curr)
                count += 1
                i -= 1
        return "".join(result)


# S = "2-4A0r7-4k"
# K = 4
S = "2-5g-3-J"
K = 2
solution = Solution()
print(solution.license_key_formatting(S, K))

class Solution:
    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        print(result)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = product + result[p2]
                result[p1] += total // 10
                result[p2] = total % 10
        sb = []
        for res in result:
            if len(sb) != 0 or res != 0:
                sb.append(res)
        return "0" if len(sb) == 0 else "".join(str(s) for s in sb)


n1, n2 = "123", "456"
solution = Solution()
print(solution.multiply(n1, n2))



print(18//10)


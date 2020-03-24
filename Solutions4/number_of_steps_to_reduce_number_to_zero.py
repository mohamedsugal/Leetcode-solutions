class Solution:
    def number_of_steps(self, num: int) -> int:
        return self.number_of_steps_rec(num, 0)

    def number_of_steps_rec(self, num: int, count: int) -> int:
        if num == 0:
            return count
        elif num % 2 == 0:
            return self.number_of_steps_rec(num // 2, count + 1)
        else:
            return self.number_of_steps_rec(num - 1, count + 1)


n = 14
s = Solution()
print(s.number_of_steps(n))

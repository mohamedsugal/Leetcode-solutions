class Solution(object):
    @staticmethod
    def decode_string(s: str) -> str:
        stack = []
        curr_str, curr_num = "", 0
        for c in s:
            if c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str, curr_num = "", 0
            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + (num * curr_str)
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_str += c
        return curr_str


val = "11[a]2[bc]"
t = Solution()
print(t.decode_string(val))

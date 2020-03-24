class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.compare(S) == self.compare(T)
    
    def compare(self, arr): 
        stack = []
        for c in arr: 
            if c != "#": 
                stack.append(c)
            elif stack: 
                stack.pop()
        return "".join(stack)
    
# S = "a##c"
# T = "#a#c"
S = "xywrrmp"
T = "xywrrmu#p"

t = Solution()
print(t.backspaceCompare(S, T))

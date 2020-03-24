from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # use A to indicate the bulls 
        # and B to indicate the cows
        # if both digitis in secret and guess its bulls
        # else is it is a cows

        bulls, cows = 0, 0 
        s, g = defaultdict(int), defaultdict(int)

        for i in range(len(secret)): 
            if secret[i] == guess[i]: 
                bulls += 1 
            else: 
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
    
        for k in s: 
            if k in g: 
                cows += min(s[k], g[k])
        
        return f'{bulls}A{cows}B'


secret = "1123"
guess = "0111"
test = Solution()
print(test.getHint(secret, guess))
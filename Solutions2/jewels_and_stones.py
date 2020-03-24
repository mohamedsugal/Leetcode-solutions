def numJewelsInStones(J: str, S: str) -> int:
    jewels = {}
    for j in J: 
        jewels[j] = jewels.get(j, 0) + 1
    count = 0
    for s in S: 
        if s in jewels: 
            count += 1 
    return count 

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))
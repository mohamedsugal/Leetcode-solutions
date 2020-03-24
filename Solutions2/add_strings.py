def addStrings(num1: str, num2: str) -> str:
    num1, num2 = list(num1), list(num2)
    carry, res = 0, []
    while len(num1) > 0 or len(num2) > 0:
        n1 = n2 = 0
        if num1: 
            n1 = ord(num1.pop()) - ord('0') 
        if num2: 
            n2 = ord(num2.pop()) - ord('0')
        temp = n1 + n2 + carry
        res.append(temp % 10)
        carry = temp // 10

    if carry: 
        res.append(carry)
    
    return ''.join([str(i) for i in res])[::-1]

    

num1 = "124"
num2 = "16"
print(addStrings(num1, num2))

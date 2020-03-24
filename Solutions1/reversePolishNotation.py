def reversePolishNotation(tokens): 
    stack = []
    for token in tokens: 
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else: 
            y = stack.pop()
            x = stack.pop()
            if token == "+": 
                stack.append(x + y)
            elif token == "-": 
                stack.append(x - y)
            elif token == "*": 
                stack.append(x * y)
            else: 
                if x * y < 0 and x % y != 0: 
                    stack.append(x / y+1)
                else: 
                    stack.append(x/y)
    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reversePolishNotation(tokens))

def balanced_parentheses(parentheses): 
    stack = []
    for paren in parentheses: 
        if paren == '(': 
            stack.append(')')
        elif paren == '{':
            stack.append('}')
        elif paren == '[': 
            stack.append(']')
        else: 
            if stack == [] or stack.pop() != paren: 
                return False 
    return stack == []

print(balanced_parentheses('({[]}]'))

    
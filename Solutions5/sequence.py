def validate_sequence(pushed, popped):
    stack = []
    index = 0
    for i in pushed:
        stack.append(i)
        while stack and stack[-1] == popped[index]:
            index += 1
            stack.pop()
    return stack == []


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validate_sequence(pushed, popped))

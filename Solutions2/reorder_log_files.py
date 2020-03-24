def reorderLogFiles(logs):
    digits = []
    letters = []
    
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key = lambda ident : ident.split()[0])
    letters.sort(key = lambda lex: lex.split()[1])    
    
    result = letters + digits             
    return result

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs))
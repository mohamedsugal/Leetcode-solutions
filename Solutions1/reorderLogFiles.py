def reorderLogFiles(logs): 
    digits = []
    letters = []
    # divide logs into two parts, one is digit logs, the other is letter logs
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key = lambda x: x.split()[0])            
    letters.sort(key = lambda x: x.split()[1:])           

    result = letters + digits                            

    return result

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# print(reorderLogFiles(logs))

full_name = lambda firstName, lastName : print(f'Hello {firstName} {lastName}')

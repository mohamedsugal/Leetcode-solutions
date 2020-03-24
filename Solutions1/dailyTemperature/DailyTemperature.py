path1 = '/Users/mohamedali/Documents/Python_Misc/InterviewPrep/dailyTemperature/test1.txt'
path2 = '/Users/mohamedali/Documents/Python_Misc/InterviewPrep/dailyTemperature/test2.txt'

with open(path2, 'r') as f: 
    digits = f.read()

def dailyTemperature(temp):
    wait_days = [0] * len(temp)

    for i in range(len(temp)): 
        j = i + 1 
        while j < len(temp) and temp[j] <= temp[i]: 
            j += 1
        if j < len(temp): 
            wait_days[i] = j - i 
    
    return wait_days
    

def dailyTemp(temp): 
    stack = []
    days_to_wait = [0] * len(temp)
    
    for i in range(len(temp)): 
        while stack and temp[i] > temp[stack[-1]]: 
            current_temp = stack.pop()
            days_to_wait[current_temp] = i - current_temp
        
        stack.append(i)
    
    return days_to_wait

temps = [int(i) for i in digits.split(',')]
print(dailyTemp(temps))
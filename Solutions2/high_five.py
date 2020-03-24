from typing import List 

from collections import defaultdict 

def highFive(items: List[List[int]]) -> List[List[int]]:
    d = defaultdict(list)
    for student, score in items:
        d[student].append(score)
        
    for i in d: 
        d[i] = sorted(d[i])[-5:]

    return [[i, sum(d[i])//5] for i in d]

        






items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],
        [1,65],[1,87],[1,100],[2,100],[2,76]]
print(highFive(items))
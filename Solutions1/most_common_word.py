from typing import List 
import re


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    '''
    >>> mostCommonWord(paragraph, banned)
    'ball'
    '''
    words = [token for token in re.findall(r"([a-zA-Z]+)",  paragraph.lower())]
    count = {}
    for word in words: 
        if word not in banned: 
            count[word] = count.get(word, 0) + 1
        else: 
            continue
    
    freq = max(count.values())
    return ''.join([k for k, v in count.items() if v == freq])

        
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
res = mostCommonWord(paragraph, banned)
print(res)
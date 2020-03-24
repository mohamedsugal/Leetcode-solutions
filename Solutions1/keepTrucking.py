def goodSegment(badNumbers, l, r):
    # [7, 15, 22, 37, 49, 60]
    # [3,6]  [8,14]  [16,21]  [23,36]  [38,48]
    # left = 3  
    # right = 48
    segments = []
    segment = None 
    for i in range(l, r+1): 
        if i in badNumbers: 
            if segment is not None: 
                segments.append(i - segment)
                segment = None 
        else: 
            if segment is None: 
                segment = i
    
    if segment is not None: 
        segments.append(r - segment+1)
    
    return segments
           
badNumbers = [37, 7, 22, 15, 49, 60]
l = 3
r = 48
print(goodSegment(badNumbers, l, r))


# def jobOffers(scores, lowerLimits, upperLimits):
#     # pairs = list(zip(lowerLimits, upperLimits))
#     # result = []
    
#     # for x in range(len(pairs)):
#     #     u = pairs[x][0]
#     #     l = pairs[x][1]
#     #     a = [x for x in scores if x in range(u, l + 1)]
        
#     #     result.append(len(a))

#     # print(result)


#     offers = []
#     for i in range(len(lowerLimits)): 
#         temp = []
#         for j in scores: 
#             if j >= lowerLimits[i] and j <= upperLimits[i]: 
#                 temp.append(j)
#         if temp is not None: 
#             offers.append(len(temp))
#         else: 
#             offers.append(0)
    
#     return offers


# scores = [4,8,7]
# lowerLimits = [2,4]
# upperLimits = [8,4]
# jobOffers(scores, lowerLimits, upperLimits)
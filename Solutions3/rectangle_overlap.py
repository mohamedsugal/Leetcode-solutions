from typing import List 

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    closest_corners = rec1[0] < rec2[2] and rec1[1] < rec2[3]
    furthest_corners = rec2[0] < rec1[2] and rec2[1] < rec1[3]
    return closest_corners and furthest_corners
    


rec1 = [1,1,4,3]
rec2 = [0,0,2,2]
print(isRectangleOverlap(rec1, rec2))


'''     y
        |      ______________ (4,3)           
        |      |            |
        |______|_____ (2,2) |
        |      |    |       |
        |(1,1) ˜˜˜˜˜|˜˜˜˜˜˜˜˜ 
        |           |               x
  (0,0) |˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜ 
        |
'''
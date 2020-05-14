# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to closest person.

# Example 1:

# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:

# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        #[0, 1, 2, 3, 0, 1, 0]
        #[0, 1, 2, 1, 0, 1, 0]
        
        res, last, n = 0, -1, len(seats)
        
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last)/2 )
                last = i
        return max(res, n - last - 1)
        
        
        
#         maxDistance = [float('inf') for seat in seats]
        
#         currDistance = float('inf')
#         for i, seat in enumerate(seats):
#             if seat == 1: 
#                 currDistance = 0
#             else:
#                 currDistance += 1
#             maxDistance[i] = currDistance
#         currDistance = float('inf')
#         for i in range(len(seats)-1, -1,-1):
#             if seats[i] == 1:
#                 currDistance = 0
#             else:
#                 currDistance += 1
#             maxDistance[i] = min(maxDistance[i], currDistance)
            
#         answer = 0
#         bestDistance = float('-inf')
        
#         for i in range(len(maxDistance)):
#             if maxDistance[i] > bestDistance:
#                 bestDistance = maxDistance[i]
#                 answer = i
#         print(maxDistance)
#         return answer
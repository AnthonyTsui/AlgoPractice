# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4
#Time complexity O(N^2)
#Space Complexity O(N)

import collections

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if len(rating) < 3:
            return 0
        
        greater, lesser = collections.defaultdict(int), collections.defaultdict(int)
        answer = 0
        
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    lesser[i] += 1
        
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    answer += greater[j]
                else:
                    answer += lesser[j]
        return answer
# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# Accepted



class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        answer = []
        prev=  float('-inf')
        for i,c in enumerate(S):
            if c == C: prev = i
            answer.append(i-prev)
        
        prev = float('inf')
        for i in range(len(S)-1, -1, -1):
            c = S[i]
            if c == C: prev = i
            answer[i] = min(answer[i], prev-i)
        return answer
        
#         answer = [0]*len(S)
#         lastSeen = None
        
#         for i in range(len(S)):
#             c = S[i]
#             if c == C:
#                 lastSeen = i
#                 answer[i] = 0
#             else:
#                 answer[i] = i - lastSeen if lastSeen is not None else float('inf')
#         lastSeen = float('inf')
#         for i in range(len(S)-1, -1, -1):
#             c = S[i]
#             if c == C:
#                 lastSeen = i
#                 answer[i] = 0
#             else:
#                 answer[i] = min(answer[i], lastSeen-i)
#         return answer
                
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# Accepted
# 261,093
# Submissions
# 578,167

#Approach: We take a BFS approach. We first obtain all perfect squares that are less than or equal to the number we have been given.
#We then iterate through each of these perfect squares, checking each possible solution and taking the "level" as our answer. 
#We then return our level when we encounter a scenario where our number is 0, meaning we've summed up to our number.

#Time complexity: O(N) ? Not certain
#Space complexity:O(N) , we are storing the perfect squares up to N

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        
        perfectSquares = []
        
        i = 1
        while (i*i) <= n:
            perfectSquares.append(i*i)
            i += 1
        
        toCheck = {n}
        answer = 0
        
        while len(toCheck):
            temp = set()
            answer += 1
            for x in toCheck:
                for y in perfectSquares:
                    if x == y:
                        return answer
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
        
        return answer
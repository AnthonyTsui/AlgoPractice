# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #to reach step 3: 1 step from step 2 or 2 steps form step 1
        #to reach step 2: 1 step from step 1 or 2 steps from step 0
        #to reachstep 1: 1 step from step 0
        
        if n <= 1: return 1

        prev, curr = 1, 2
        index =  2
        while index < n:
            new = prev + curr
            prev = curr
            curr = new
            index += 1
        return curr
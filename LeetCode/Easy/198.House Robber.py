# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, 
# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


#DP style question, we know for any i-th house, we have two choices: 
#rob the house, which yields rob(i-2) + houseValue 
#or don't rob the house, which yields rob(i-1) 
#We need to maintain two running values: the max value if we do and don't rob the current house

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0 
        houses = [0 for x_ in range(len(nums)+1)]
        houses[0], houses[1] = 0, nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            houses[i+1] = max(houses[i], houses[i-1]+num)
        return houses[-1]
        
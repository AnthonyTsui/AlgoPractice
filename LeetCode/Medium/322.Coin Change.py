# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:

#Approach: We can recognize that this is a DP problem due to the fact that the optimal solution to any ith amount is the summation of its 
#optimal solutions to its subproblems.
#For example given one coin with C value and an amount N, we know that min(N) = 1 + min(N-C), or the minimum number of coins to make N is the minimum
#number of coins needed to make N-C, the remaining value.
#To solve this dynamically,we create a list with length amount + 1 in order to calculate all the minimum coins required to make the values
#leading up to the target amount. We can then utilize min(denoms[i], 1 + denoms[i-c]) to calculate the minimum coins needed at 'i' amount



#Time complexity: O(C*N) where C = len(coins) and N = amount + 1
#Space Complexity: O(N) 

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #For the amount, maxDenoms = mAmount
        #For any coin, maxDenoms = m(Amount - coinValue)
        
        denoms = [float("inf") for i in range(amount+1)]
        denoms[0] = 0
        print(coins, amount)
        for coin in coins:
            for i in range(coin, amount+1):
                denoms[i] = min(denoms[i], 1 + denoms[i-coin])
        return -1 if denoms[-1] == float('inf') else denoms[-1]
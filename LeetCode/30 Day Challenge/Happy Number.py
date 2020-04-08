# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

#Approach, we simply check each product square of the number, if they are the same then we 
#break and check to see if this is because they are equal and not == 1 (meaning we've begun looping) or if they are == 1
#In the case that they are equal to 1, it means that it is a happy number and we can return true
#Not sure on time and space complexity

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast, slow = n, n
        while True:
            slow = getSumSquare(slow)
            fast = getSumSquare(getSumSquare(fast))
            if slow != fast:
                continue
            else:
                break
        return slow == 1
        
        
def getSumSquare(n):
    sumSquare = 0
    while n > 0:
        sumSquare += (n%10)*(n%10)
        n = int(n/10)
    return sumSquare
# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example :

# Input: n = 10, pick = 6
# Output: 6

#Time Complexity: O(logn)
#Space Complexity :O(1)


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = n
        upper,lower = n, 1
        response = guess(n)
        while response != 0:
            if response == -1:
                upper = min(upper, curr)
                curr = (curr + lower) // 2
            elif response == 1:
                lower = max(lower, curr)
                curr = (curr + upper) // 2
            else:
                return curr
            response = guess(curr)
        return curr
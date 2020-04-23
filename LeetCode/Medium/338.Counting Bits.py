# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

#Time complexity: O(N)
#Spce complexity:O(1)

#We will notice a pattern emerges as we run through examples of the algorithm: 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4
#if we try to find a pattern: we will find that f(x) = f(x-offset) + 1 where offset is a power of two, and differs after "offset" number of times
#For example: f(0) = 0 ,  f(1) = f(1-1) + 1 = 1,  f(2) = f(2 - 2) + 1 = 1, f(3) = f(3 - 2) + 1 = 2, f(4) = f(4 - 4) + 1 = 1, f(5) = f(5 - 4) + 1 = 2 and so on...

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = [0, 1, 1, 2]
        if num <= 3: return output[:num+1]
        curr = 4
        offset = 4
        iterations = 0
        while curr <= num:
            if iterations == offset:
                iterations = 0
                offset = offset*2
            output.append(output[curr-offset]+1)
            iterations += 1 
            curr += 1
        return output
        
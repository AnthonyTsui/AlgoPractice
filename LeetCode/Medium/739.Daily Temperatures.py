# Given a list of daily temperatures T, return a list such that, for each day in the input, 
# tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

#Approach: If we traverse the list backwards, we can keep track of the highest temperatures we've found so far that are still relevant to the question.
#For example with a list being [...78, 79, 80, 76, 74]: Knowing [76, 74] won't help us as 80 > both of them
#This means we should maintain a stack of temperatures such that if the current temperature we're at is greater, remove the elements that are less than it (as our current index
# is now our most "next-to-day" temperature.) In the case that there is a temperature less than the top of our stack, we know that the difference between our current index
#and the index (at the top of the stack) is the nubmer of days away. Afterwards we can just append the current temperature to the top of our stack

#Time complexity :O(N), space complexity :O(N) , in the case where the temperature is listed in ascending order, we would be storing all the elements in the stack

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        toWait = [0 for t in T]
        stack = []
        
        for i in reversed(range(len(T))):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                toWait[i] = stack[-1] - i
            stack.append(i)
        return toWait
            
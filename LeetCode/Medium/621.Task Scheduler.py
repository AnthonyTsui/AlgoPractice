# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

#Time complexity: O(N) for creating task_count, finding max count and max occurances
#Space Complexity:O(N) for storing all tasks and their occurancces

import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = collections.Counter(tasks).values()
        maxCount = max(task_count)
        maxOccurances = task_count.count(maxCount)
        return max(len(tasks), maxOccurances + (maxCount-1)*(n+1))
             
        
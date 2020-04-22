# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), where h is the height of the person 
# and k is the number of people in front of this person who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

 
# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


#Time complexity: O(N^2) since we iterate through the array and append a value which takes O(N) * O(N) time 
#Space complexity: O(N) since we store the sorted list of people

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return []
        
        sorted_people = sorted(people, key = lambda x: (-x[0], x[1]))
        
        output = []
        
        for p in sorted_people:
            output.insert(p[1], p)
        
        return output
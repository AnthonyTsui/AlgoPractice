# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

#Approach: We can iterate through the nums array to create a dict, then iterate through the dict:
#The first time we will create a dictionary with the count of each nums
#The second time we will create a new dictionary that takes the count of each element, and uses it as a key with the number as the value
#Since we know the most amount of time an element can appear is len(nums), (as in it is the only number that appears): 
#We can can iterate through the len (nums), going -1 each step, and add all the values of that count in our second dictionary our output array

#To illustrate it better: 
# Say our nums array is length 3: We check to see if there are elements that have a count of 3 in our second dictionary, and then we add every single one of those nums to our output
#Then we go 3-1 = 2: We check to see if there are elements with a count of 2.. and so on. This way we ensure that we are adding our elements with the highest count 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count, frequency = {}, {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            
        for num, freq in count.iteritems():
            if freq not in frequency:
                frequency[freq] = [num]
            else:
                frequency[freq].append(num)
                
        answer = []
        
        for i in range(len(nums), 0, -1):
            if i in frequency:
                for val in frequency[i]:
                    answer.append(val)
            if len(answer) >= k: return answer[:k]
        
        return answer[:k]
            

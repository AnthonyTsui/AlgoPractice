# Given an array of integers nums and an integer k, determine whether 
# there are two distinct indices i and j in the array where nums[i] = nums[j] 
# and the absolute difference between i and j is less than or equal to k.

# Approach: iterate through the array, and as you progress keep track of where the last saw 
#a number. We can assume that if there are multiple instances of a value, we can immediately
#compare our newest found instance with our last found instance. If it is not <= k, we have no need
#for the last found and can save our newly found in its place

#Time Complexity: O(N) where n is the number of elements in nums, space is at most O(E) where e is the number of distinct elements in nums

def containsCloseNums(nums, k):
    dict = {}
    for i , num in enumerate(nums):
        if num in dict and abs(dict[num] - i) <= k:
            return True
        dict[num] = i
    return False
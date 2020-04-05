
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

#Approach is simple, we understand that for every ith element, the corresponding output is the product of all (1...ith-1) element times (ith+1....Nth) product
#For exmaple in [1,2,3,4] : F(1) = []*[2*3*4]  
#F(2) = [1]*[3*4],  F(3) = [1*2]*[4],   F(4) = [1*2*3]*[]

#This means we can create two arrays, one holding the left-handed products, and one holding the right-handed products. 
#We can then construct our output for an ith element by multipling the ith element of left and right handed products together
#To accomplish this in O(1) time, we let either the left or right handed array be our output array.
#We then traverse the array again in the opposite direction, saving a number to be our running total of the right handed products, and construct our final answer as we go.

#Time complexity: O(N), Space Complexity:O(1)
#Time wise we traverse the array twice, so 2N -> O(N)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [num for num in nums]
        output[0] = 1
        currNum = 1
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
        
        for i in reversed(range(len(nums)-1)):
            currNum *= nums[i+1]
            output[i] = output[i]*currNum

        return output
        
        
#         leftProducts = [num for num in nums]
#         rightProducts= [num for num in nums]
#         leftProducts[0], rightProducts[-1] = 1, 1
        
#         for i in range(1, len(nums)):
#             leftProducts[i] = leftProducts[i-1] * nums[i-1]
#         for i in reversed(range(len(nums)-1)):
#             rightProducts[i] = rightProducts[i+1]*nums[i+1]
        
#         output = [left*right for left, right in zip(leftProducts, rightProducts)]
#         return output
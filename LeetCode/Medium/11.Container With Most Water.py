# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


#Approach: There are two factors to consider between each two points:
#The smaller of the two heights, as well as the difference in index between the two
#As this gives us the Width X Height = Volume
#Meaning for volume, the largest volume is the largest of the min() of two lines, with the greatest distance
#We can do a O(N^2) approach where we iterate through each index, and check the volume of each one after it 

#As we try to implement the above approach, (or even before that) we can see that at the two farthest element,
#we have the largest width possible. This means to obtain a larger area, we have to check the inward elements whichh
#results in a smaller width. The only way to increase our area then, is to have a larger min element. As 
#the smalelr of the two heights will always be the limiting factor of the two. 

#This way we simply check the area and compare it with our max area, before moving inwards based on which element
#is smaller.

#Time Complexity: O(N)
#Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        maxArea = (right-left)*min(height[left], height[right])
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            maxArea = max(maxArea, (right-left)*min(height[left], height[right]))
        return maxArea
# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();


from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.original = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            idx = randint(i, len(self.array)-1)
            self.array[i], self.array[idx] = self.array[idx], self.array[i]
        return self.array

# class Solution(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.original = nums[:]
        

#     def reset(self):
#         """
#         Resets the array to its original configuration and return it.
#         :rtype: List[int]
#         """
#         return self.original

#     def shuffle(self):
#         """
#         Returns a random shuffling of the array.
#         :rtype: List[int]
#         """
#         seen = set()
#         res = []
#         while len(seen) != len(self.original):
#             idx = randint(0, len(self.original)-1)
#             if idx not in seen:
#                 seen.add(idx)
#                 res.append(self.original[idx])
#         return res
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
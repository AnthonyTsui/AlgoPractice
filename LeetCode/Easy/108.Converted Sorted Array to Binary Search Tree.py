# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


# Definition for a binary tree node.
#Time Complexity: O(N) where N = len(nums)
#Space Complexity: O(N) as our call stack grows to the height of the answer tree
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        depth = len(nums)//2
        root = TreeNode(nums[depth])
        root.left = self.sortedArrayToBST(nums[:depth])
        root.right = self.sortedArrayToBST(nums[depth+1:])
        
        return root


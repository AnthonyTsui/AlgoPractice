# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time complexity is O(N) as we only traverse all the nodes in the tree once (which is n number of nodes)
#Space complexity is O(N) as we are storing our paths for each node

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        cache = {0:1}
        self.answer = 0
        self.dfs(root, 0, cache, sum)
        return self.answer
        
    def dfs(self, node, currentPathSum, cache, target):
        if node is None:
            return 
        currentPathSum += node.val
        oldPathSum = currentPathSum-target
        self.answer += cache.get(oldPathSum, 0)
        cache[currentPathSum] = cache.get(currentPathSum, 0)+1
        
        self.dfs(node.left, currentPathSum, cache, target)
        self.dfs(node.right, currentPathSum, cache, target)
        
        cache[currentPathSum] -= 1
        
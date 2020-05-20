# Given a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:



# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

#Time Complexity: O(N) where N = nodes in tree
#Space Complexity: O(N), in a full balanced binary tree, the last level is roughly N/2 nodes, and the second to last is N/4. Meaning at most
#we are storing N/2 + N/4 nodes at a time

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        prev, curr = [], [root]
        while curr:
            prev = curr
            curr = [child for node in curr for child in [node.left, node.right] if child]
        return sum(node.val for node in prev)
    
#         mapping = collections.defaultdict(list)
#         def dfs(node, depth):
#             if not node:
#                 return
#             mapping[depth].append(node.val)
#             dfs(node.left, depth+1)
#             dfs(node.right, depth+1)
#         dfs(root, 1)
#         return sum(mapping[max(mapping.keys())])
        
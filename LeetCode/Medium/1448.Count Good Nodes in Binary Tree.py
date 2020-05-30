# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


# Example 1:

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
 #   def goodNodes(self, root: TreeNode) -> int:
#         stack = [(root, float('-inf'))]
#         ans = 0
        
#         while stack:
#             node, currMax = stack.pop()
#             if not node:
#                 continue
#             if node.val >= currMax:
#                 ans += 1
#             currMax = max(currMax, node.val)
#             stack.append((node.left, currMax))
#             stack.append((node.right, currMax))
#         return ans
               
    
     def goodNodes(self, root: TreeNode) -> int:
        res = 0
        currMax = float('-inf')
        def dfs(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                nonlocal res
                res += 1
            currMax = max(currMax, node.val)
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        dfs(root, currMax)
        return res
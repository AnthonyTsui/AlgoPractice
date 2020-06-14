# Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

# In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

# Return the number of moves required to make every node have exactly one coin.

 

# Example 1:



# Input: [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

#Time Complexity: O(N) where N = num of nodes in the tree
#Space Complexity:O(H), the largest our call stack grows is the max height (H) of the tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R -1
        
        dfs(root)
        return self.ans
        
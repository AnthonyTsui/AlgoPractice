# Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #For target X, we need to find all nodes that to X, then all nodes to that lead to those nodes and so on..
        def dfs(cur, path):
            if cur == len(graph)-1: res.append(path)
            else:
                for node in graph[cur]: dfs(node, path+[node])
        res = []
        dfs(0, [0])
        return re=
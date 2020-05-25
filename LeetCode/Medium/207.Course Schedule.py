# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.


#Time Complexity: O(V+E), where V, E = vertices and edges of the graph. The most our dfs() function will visit in one call is our entire graph, which is V+E
#Space Complexity: O(V+E)

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
        
        def dfs(x):
            if visited[x] == -1:
                return False
            if visited[x] == 1:
                return True
            visited[x] = -1
            for y in graph[x]:
                if not dfs(y):
                    return False
            visited[x] = 1
            return True
        
        for i in range(numCourses-1):
            if not dfs(i):
                return False
        return True
            
                
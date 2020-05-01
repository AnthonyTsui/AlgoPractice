# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter

#Time complexity: O(N * L^2) where N = len(A) and L = length of longest string
#Space complexity :O(L) 

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        answer = list(A[0])
        for i in range(1,len(A)):
            curr = A[i]
            overlap = []
            for c in curr:
                if c in answer:
                    answer.remove(c)
                    overlap.append(c)
            answer = overlap
        return answer
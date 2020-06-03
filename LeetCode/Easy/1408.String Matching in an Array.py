# Given an array of string words. Return all strings in words which is substring of another word in any order. 

# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []

#Approach: Sort the words by length, then compare each substr in the sotred array with the elements ahead of it. Break if we notice it is a substr
#Time Complexity: O(nlogn + n^2)
#Space Complexity: O(n)

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sortedWords = sorted(words, key=len)
        res = []
        for i, substr in enumerate(sortedWords):
            idx = i+1
            for j in range(idx, len(sortedWords)):
                if substr in sortedWords[j]:
                    res.append(substr)
                    break
        return res
            
        
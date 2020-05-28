# Given a sentence that consists of some words separated by a single space, and a searchWord.

# You have to check if searchWord is a prefix of any word in sentence.

# Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

# If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

# A prefix of a string S is any leading contiguous substring of S.

 

# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
# Example 2:

# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
# Example 3:

# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.
# Example 4:

# Input: sentence = "i use triple pillow", searchWord = "pill"
# Output: 4


#sentences.split() will take len(sentence), and for each comparison, we at most do len(searchWord) and then again for the comparison
#Time Complexity: O(N*S) where N = len(sentence) and S = len(searchWord)
#Space Complexity: O(N) since we sentence.split()

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        slength = len(searchWord)
        words = sentence.split()
        for i in range(len(words)):
            if len(words[i]) >= slength and words[i][:slength] == searchWord:
                return i+1
        return -1
        
        # for i,word in enumerate(sentence.split()):
        #     if len(word) >= slength and word[:slength] == searchWord:
        #         return i+1
        # return -1
            
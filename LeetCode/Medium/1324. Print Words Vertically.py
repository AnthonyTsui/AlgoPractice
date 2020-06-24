# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

 

# Example 1:

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
#  "HAY"
#  "ORO"
#  "WEU"
# Example 2:

# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"
# Example 3:

# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]


#Time Complexity: O(n*S) where n = len(s) and s is the length of the longest word in the list 
#Space complexity:O(n) or O(nS)


from typing import List
class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split()
        maxLength = max(words, key=len)
        length = len(maxLength)
        
        
        for i in range(length):
            curr = ''
            for word in words:
                if i >= len(word):
                    curr = curr + ' '
                    continue
                curr = curr + word[i]
            ans.append(curr.rstrip())
        return ans
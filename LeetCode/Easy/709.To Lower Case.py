# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"


#Time Complexity :O(N)
#Space Complexity: O(N)

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = ''
        for s in str:
            if ord(s) >= 65 and ord(s) < 97:
                ans += chr(97 + (ord(s) - 65))
            else:
                ans += s
        return ans
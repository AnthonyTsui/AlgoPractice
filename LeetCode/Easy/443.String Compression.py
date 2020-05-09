# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.

 
# Follow up:
# Could you solve it using only O(1) extra space?

 
# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

# Example 2:

# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.


#Time Complexity: O(N)
#Space Complexity: O(1)

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)
        
        anchor, write = 0, 0
        
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read+1] != c:
                chars[write] = c
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.


#Time complexity: O(3^N * 4^M) where N = number of digits that map to 3 letters, M = number of digits that map to 4 letters
#Space Complexity: O(3^N * 4^M) due to storing the results
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #23
        #[a,b,c][ad,bd,cd,ae,be,ce,af,bf,cf]
        
        output = []
        if not len(digits): return output
        
        mapping = { 
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        def backtracking(combination ,nextDigits):
            if not len(nextDigits):
                output.append(combination)
            else:
                for letter in mapping[nextDigits[0]]:
                    backtracking(combination+letter, nextDigits[1:])
        
        if len(digits):
            backtracking('', digits)
        return output
#         output.extend(mapping[digits[0]])
        
#         for i in range(1, len(digits)):
#             curr = digits[i]
#             oldLen = len(output)
#             for letter in mapping[curr]:
#                 for j in range(oldLen):
#                     output.append(output[j]+letter)
#             output = output[oldLen:]
#         return output
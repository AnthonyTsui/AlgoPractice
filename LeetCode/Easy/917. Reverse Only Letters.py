# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = ['a']*len(S)
        
        stack = []
        for i in range(len(S)):
            if not S[i].isalpha():
                ans[i] = S[i]
            else:
                stack.append(S[i])
        
        for i in range(len(ans)):
            if not ans[i].isalpha():
                continue
            curr = stack.pop()
            ans[i] = curr
        return ''.join(ans)
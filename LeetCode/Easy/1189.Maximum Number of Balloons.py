# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:

# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

#Time Complexity: O(N)
#Space Complexity: O(1)
import collections
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = collections.Counter()
        for c in text:
            if c in 'balon':
                freq[c] += 1
        b, a, l ,o, n = freq['b'], freq['a'], freq['l']//2, freq['o']//2, freq['n']
        return min(b,a,l,o,n)
        
        
        # while True:
        #     for c in 'ban':
        #         if freq[c] < 1:
        #             return answer
        #         freq[c] -= 1
        #     for c in 'lo':
        #         if freq[c] < 2:
        #             return answer
        #         freq[c] -= 2
        #     answer += 1
        # return answer
        # while freq['b'] >= 1  and freq['a'] >= 1 and freq['l'] >= 2 and freq['o'] >= 2 and freq['n'] >= 1:
        #     answer += 1
        #     for c in 'ban':
        #         freq[c] -= 1
        #     for c in 'lo':
        #         freq[c] -= 2
        # return answer
        
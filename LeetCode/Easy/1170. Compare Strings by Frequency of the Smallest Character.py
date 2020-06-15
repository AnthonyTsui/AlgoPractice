# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

# Example 1:

# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# Example 2:

# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


#Time Complexity: O(w + wlogw + l*w) where w = len(words), l = len(list)
#Space Complexity: O(w + l)

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordFreq = []
        
        def getFreq(string):
            smallest = None
            for c in string:
                if smallest is None or ord(c) < ord(smallest):
                    smallest = c
            return string.count(smallest)
        
        for word in words:
            wordFreq.append(getFreq(word))
        wordFreq.sort()
        
        ans = []
        for q in queries:
            curr = 0
            freq = getFreq(q)
            if freq >= wordFreq[-1]:
                ans.append(0)
            else: 
                for i in range(len(wordFreq)):
                    if wordFreq[i] > freq:
                        ans.append(len(wordFreq)-i)
                        break
        return ans
    

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

#Approach: We know that strings that are anagrams of each other will have the same sorted string
#For example : tea: ate, eat, aet. We can create a dictionary using the sorted words as the key and 
#store them into the value array. Our output then will be just be a list with all the values
#Time complexity: O(Nklogk) where k is the length of the longest string
#Space Complexity: O(NK) 


#Another approach instead of sorting the strings individual, we can create a list of size 26
# in order to check the frequency of each letter in the string. Strings with the same frequencies are anagrams of eahc other
#this way when we "sort" each string, it takes O(K) instead of O(KlogK)
#Time complexity: O(NK) where k is the length of the longest string
#Space Complexity: O(NK) 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        # ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = [] 
            ans[tuple(count)].append(s)
        return ans.values()
        
        
        # anagrams = {}
        # for string in strs:
        #     freq = [0]*26
        #     for c in string:
        #         freq[ord(c)-ord('a')] += 1
        #     anagrams[tuple(freq)].append(string)
        # return anagrams.values()
        
        # anagrams = {}
        # for string in strs:
        #     sortedStr = ''.join(sorted(string))
        #     if sortedStr not in anagrams:
        #         anagrams[sortedStr] =  []
        #     anagrams[sortedStr].append(string)
        # return anagrams.values()
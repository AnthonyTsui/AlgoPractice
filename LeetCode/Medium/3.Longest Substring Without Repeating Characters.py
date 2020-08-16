# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


#From each index of the string: iterate through the rest of the string, building a substring 
#and checking that there are no duplicates. 

#The main optimization point here is realizing that when we encounter a duplicate,
#we want to continue search by setting the new substring to begin where the first of the duplicate is found.
#For example: abcded -> [a] [ab] [abc] [abcd] [abcde] -> at this point we encounter another d. We should realize then that we 
#should skip 'b' and 'c' as the duplicates of d are still ahead of it, and it is impossible to get a larger substring than we previously checked.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions = {}
        left = currmax = 0 
        for i, c in enumerate(s):
            if c in positions and left <= positions[c]:
                left = positions[c] + 1
            else:
                currmax = max(currmax, i - left + 1)
            positions[c] = i
        return currmax
        
        # currmax = 0
        # left, right = 0, 0
        # substring = []
        # while left < len(s) and right < len(s):
        #     rchar = s[right]
        #     if rchar in substring:
        #         currmax = max(currmax, len(substring))
        #         while substring and rchar in substring:
        #             lchar = s[left]
        #             substring.remove(lchar)
        #             left += 1;
        #     else:
        #         substring.append(rchar)
        #         right += 1;
        # if substring: currmax = max(currmax, len(substring))
        # return currmax
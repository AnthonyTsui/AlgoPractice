# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:

# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
 
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
 
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin. 

 

# Example 1:

# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example 2:

# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

# Notes:

# S contains only uppercase, lowercase and spaces. Exactly one space between each word.
# 1 <= S.length <= 150.

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        output = []
        for i, word in enumerate(S.split()):
            if word[0] not in vowels:
                word = word[1:] + word[:1]
            output.append(word+'ma'+'a'*(i+1))
        return ' '.join(output)
        
        
        # def getLatin(word, i):
        #     if word[0] not in vowels:
        #         word = word[1:] + word[:1]
        #     return word + 'ma' + ('a'*(i+1))
        # return ' '.join(getLatin(word, i) for i, word in enumerate(S.split()))
        
        
        # def latin(w, i):
        #     if w[0] not in vowels:
        #         w = w[1:] + w[:1]
        #     return(w+'ma'+'a'*(i+1))
        # return ' '.join(latin(w, i) for i, w in enumerate(S.split()))
        
        
        
        # for i, word in enumerate(words):
        #     firstLetter = word[0]
        #     print(firstLetter in vowels)
        #     if firstLetter in vowels:
        #         words[i] += "ma"
        #     else:
        #         words[i] = word[1:] + word[:1] + 'ma'
        #     words[i] += 'a'*(i+1)
        # return "".join(word+" " if i < len(words)-1 else word for i, word in enumerate(words))

#Straight forward easy solution but runs poorly in time and memory, ~6% for both if we use the function inside. Else, if we don't define it it's about 90% Time complexity

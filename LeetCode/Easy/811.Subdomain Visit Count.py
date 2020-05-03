# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# Example 1:
# Input: 
# ["9001 discuss.leetcode.com"]
# Output: 
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation: 
# We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

# Example 2:
# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: 
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.


#APproach: Iterate  through each visit input and add the visit number to each domain, then just return the dictionary items

#Time complexity: O(N)
#Space complexity: O(N*3)

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        mapping = {}
        
        for visit in cpdomains:
            count, domain = visit.split()
            count = int(count)
            splitDomain = domain.split('.')
            for i in range(len(splitDomain)):
                subDomain = '.'.join(splitDomain[i:])
                if subDomain not in mapping:
                    mapping[subDomain] = 0
                mapping[subDomain] += count
        
        return [str(v) + ' ' + d for d,v in mapping.items()]
        
        
#         mapping = {}
        
#         for visit in cpdomains:
#             splitVisit = visit.split()
#             visits = int(splitVisit[0]) 
#             domain = splitVisit[1]
            
#             toVisit = []
#             dotIdx = domain.find('.')
            
#             while dotIdx != -1:
#                 toVisit.append(domain)
#                 domain = domain[dotIdx+1:]
#                 dotIdx = domain.find('.')
            
#             toVisit.append(domain)
            
#             for subdomain in toVisit:
#                 if subdomain not in mapping:
#                     mapping[subdomain] = 0
#                 mapping[subdomain] += visits
        
#         answer = []
        
#         for d,v  in mapping.iteritems():
#             answer.append(str(v) + ' ' + d)
        
#         return answer
            
            
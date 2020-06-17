# Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.
# # 

# The Fibonacci numbers are defined as:

# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 , for n > 2.
# It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.
 

# Example 1:

# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# Example 2:

# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# Example 3:

# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.


#Proof from user box_of_donuts on LC
# Base case: i = 1. We replace the first pair of numbers in the sequence, call them F_k, with F_(k-2) and F_(k+1). Adding F_(k-2) clearly will not result in duplicates as it is the smallest number in the sequence now. Adding F_(k+1) also cannot lead to duplicates. Why? Because, our assumption is that we start with a sequence with no adjacent Fibonacci numbers present. Hence because we have F_k, we cannot have F_(k+1) present. Further, because the sequence is minimal, we also cannot have F_(k+2) present, because if it were then by removing (the newly added) F_(k+1) along with F(k+2) and replacing them with F_(k+3), we have created a smaller sequence that still sums to our target, contradicting minimality. So we have shown the claim is true for our base case.

# Induction Hypothesis: If for some number n it holds that, the sequence has the n'th Fibonacci numbers in the sequence duplicated and this n is maximal and no adjacent elements are present, then the de-duplication process will always lead to removing duplicates across the entire sequence and preserving the number of sequence elements.

# Inductive Step: i = n+1. Say that the (n+1)th such duplicated Fibonacci numbers in the sequence are F_k, with n+1 maximal and no adjacent elements present, and we replace them with F_(k+1) and F_(k-2). Adding F_(k+1) will not result in duplicates and will not result in adjacent elements for the same reason as in the base case. Adding F_(k-2) cannot lead to adjacent elements: F_(k-1) is not present, and the same logic as in the base case shows that this sequence cannot possibly have F_(k-3) present (because otherwise we could have created a smaller sequence, contradicting minimality). However, adding F_(k-2) could potentially yield duplicates if F_(k-2) is already present, OR we could have started with duplicates already present earlier in the sequence. In this case, we invoke the induction hypothesis for i = n, which shows that the earlier part of the sequence can have all elements de-duplicated with sequence length preserved.

# This proves the claim.

# However there is one caveat: what if there are MORE than two copies of a Fibonacci number present in such a sequence? The answer to that is that this is not possible: if we had 3*F_k present, we know that this sum is equivalent to 2*F_k + F_k = F_(k-2) + F_(k+1) + F_k = F_(k-2) + F_(k+2). Hence the existence of such a triplet would contradict minimality.
        

#Time Complexity: O(logk)
#Space Complexity: O(1)
#Iterative Approach
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2 : return k
        a, b, res = 1, 1, 0
        
        while b <= k:
            a, b = b, b + a
            
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b-a, a
        return res                
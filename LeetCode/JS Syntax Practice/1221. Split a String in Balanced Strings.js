// Balanced strings are those who have equal quantity of 'L' and 'R' characters.

// Given a balanced string s split it in the maximum amount of balanced strings.

// Return the maximum amount of splitted balanced strings.

 

// Example 1:

// Input: s = "RLRRLLRLRL"
// Output: 4
// Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
// Example 2:

// Input: s = "RLLLLRRRLR"
// Output: 3
// Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
// Example 3:

// Input: s = "LLLLRRRR"
// Output: 1
// Explanation: s can be split into "LLLLRRRR".
// Example 4:

// Input: s = "RLRRRLLRLL"
// Output: 2
// Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

/**
 * @param {string} s
 * @return {number}
 */
/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let count = 0;
    let ans = 0;
    
    for(let i = 0; i < s.length; i++){
        if (s[i] == 'R'){count++;}
        else{count--;}
        
        if (count == 0){ ans++;}
    }
    return ans
    
    
//     let left, right, ans;
//     left = right = ans = 0;
    
//     for(i=0;i<s.length;i++){
//         if (s[i] == 'L'){left++;}
//         else{right++;}
//         if (left == right){
//             ans++;
//             left = right = 0
//         }
//     }
//     return ans
    
//     let left, right, ans;
//     left = right = ans = 0;
    
//     [...s].forEach(function(c){
//         if (c == 'L') { left += 1}
//         else { right += 1}
        
//         if (left == right){
//             ans += 1
//             left = right = 0
//         }
//     })
//     return ans
};
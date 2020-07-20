// Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

// Return the answer in an array.

 

// Example 1:

// Input: nums = [8,1,2,2,3]
// Output: [4,0,1,1,3]
// Explanation: 
// For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
// For nums[1]=1 does not exist any smaller number than it.
// For nums[2]=2 there exist one smaller number than it (1). 
// For nums[3]=2 there exist one smaller number than it (1). 
// For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).


/**
 * @param {number[]} nums
 * @return {number[]}
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    var sorted = Array.from(nums).sort((a, b) => b - a)
    //var smaller = new Map(sorted.map((num, index) => [num, nums.length - index - 1]))
    var smaller = new Map(sorted.map(function(num, index){
        //console.log(num, nums.length-index-1)
        return [num, nums.length-index-1]
    }));
    return nums.map(num => smaller.get(num))
//     var sorted = [...nums].sort((a,b) => a - b)
//     var dict = {}
//     let smaller = 0
//     let curr = sorted[0]
//     dict[sorted[0]] = smaller
//     for(i=1; i<sorted.length;i++){
//         smaller += 1
//         if (curr == sorted[i]) {continue}
//         curr = sorted[i]
//         dict[curr] = smaller
//     }
//     var ans = new Array()
//     for(i=0; i < nums.length; i++){
//         ans.push(dict[nums[i]])
        
//     }
//     return ans
};
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashTable = {};
    for(let i = 0; i < nums.length; i++) {
        if(hashTable[target - nums[i]] != undefined) {
            return [hashTable[target - nums[i]], i];
        } else {
            hashTable[nums[i]] = i;    
        };
    };
};
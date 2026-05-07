class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const twoSumFinder = {};

        for(let i = 0; i < nums.length; i++){
            const reqNum = target - nums[i];

            if(reqNum in twoSumFinder){
                return [i, twoSumFinder[reqNum]];
            }
            twoSumFinder[nums[i]] = i;
        }
    }
}

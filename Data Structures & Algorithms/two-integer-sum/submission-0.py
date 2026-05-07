class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumRecord = {}
        for i in range(len(nums)):
            reqNum = target - nums[i]
            if reqNum in twoSumRecord:
                return [twoSumRecord[reqNum], i]
            twoSumRecord[nums[i]] = i
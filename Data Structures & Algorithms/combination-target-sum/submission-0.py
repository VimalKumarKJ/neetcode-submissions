class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            if curr_sum > target or index == len(nums):
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                path.pop()
        backtrack(0, 0)
        return res
            
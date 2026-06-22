class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        nums.sort()

        def backtrack(start, curr_sum):
            #Success/Conclusive cases or failure cases
            if curr_sum == target:
                res.append(path.copy())
                return
            
            
            for i in range(start, len(nums)):
                if curr_sum + nums[i] > target:
                    break
                
                path.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                path.pop()
        backtrack(0, 0)
        return res
            
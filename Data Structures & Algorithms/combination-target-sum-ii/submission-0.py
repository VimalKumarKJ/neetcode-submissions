class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()

        def backtrack(index, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
        
            if index >= len(candidates) or curr_sum > target:
                return
        
            for i in range(index, len(candidates)):
                if curr_sum + candidates[i] > target:
                    break
                
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                    
                path.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i])
                path.pop()
        backtrack(0, 0)
        return res
            
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] # horizontal flow values
        path = [] # vertical flow values

        nums.sort()

        def backtrack(index):
            res.append(path.copy())

            if index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                #check for pruning horizontal dups
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])

                backtrack(i+1) #vertical movements/shifts

                path.pop()

        backtrack(0)
        return res




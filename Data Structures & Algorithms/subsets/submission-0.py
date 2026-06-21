class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initializers
        res = []
        path = []

        # Declare the backtrack function
        def backtrack(start):
            # Success / Conclusion case [Or All values are valid]
            res.append(path.copy())
            # Logic
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        return res
            


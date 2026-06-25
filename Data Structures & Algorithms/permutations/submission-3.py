class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        unique = set()

        def backtrack(index):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in unique:
                    continue
                
                path.append(nums[i])
                unique.add(nums[i])

                backtrack(i+1)

                path.pop()
                unique.remove(nums[i])
        backtrack(0)
        return res

            
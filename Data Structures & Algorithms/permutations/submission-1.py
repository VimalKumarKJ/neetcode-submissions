class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        unique = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in unique:
                    continue
                
                path.append(num)
                unique.add(num)

                backtrack()

                path.pop()
                unique.remove(num)
        backtrack()
        return res

            
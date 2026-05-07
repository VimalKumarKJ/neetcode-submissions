class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if i != j:
                    res *= nums[j]
            temp.append(res)
        return temp
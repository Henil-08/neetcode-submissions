class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        product = 1
        for num in nums:
            if num == 0:
                count += 1
            else:
                product *= num
        
        if count > 1: return [0] * len(nums)

        res=[0] * len(nums)
        for i, num in enumerate(nums):
            if count == 1: 
                res[i] = 0 if num != 0 else product
            else:
                res[i] = product // num

        return res

        
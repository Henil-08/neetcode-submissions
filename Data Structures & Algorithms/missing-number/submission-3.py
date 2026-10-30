class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for idx in range(len(nums)-1):
            if (nums[idx+1] - nums[idx]) != 1:
                return (nums[idx+1] + nums[idx]) // 2

        if nums[0] == 0:
            return len(nums)
        else: return 0
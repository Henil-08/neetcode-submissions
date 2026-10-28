class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            hashmap[num] = idx

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != idx:
                return [idx, hashmap[complement]]

        return []
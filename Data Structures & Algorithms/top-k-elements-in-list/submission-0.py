class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        arr = []
        for value, count in hashmap.items():
            arr.append([count, value])
        arr.sort()

        final = []
        for i in range(k):
            final.append(arr.pop()[1])
                
        return final

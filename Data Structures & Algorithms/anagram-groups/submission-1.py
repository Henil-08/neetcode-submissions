class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for string in strs:
            sortedS = ''.join(sorted(string))
            final[sortedS].append(string)

        return list(final.values())
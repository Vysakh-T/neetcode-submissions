class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}
        for i in range(len(strs)):
            ssorted = tuple(sorted(strs[i]))
            if seen.get(ssorted)==None:
                seen[ssorted]=[strs[i]]
            else:
                seen[ssorted].append(strs[i])
            
        return list(seen.values())
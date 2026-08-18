class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts[char] = counts.get(char,0) + 1
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True
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
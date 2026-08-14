class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for i in s:
            smap[i] = 1 if not smap.get(i) else smap[i]+1
        for i in t:
            if not smap.get(i):
                return False
            smap[i]-=1
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = dict()
        for i in s:
            smap[i] = 1 if not smap.get(i) else smap[i]+1
        tmap = dict()
        for i in t:
            tmap[i] = 1 if not tmap.get(i) else tmap[i]+1
        return smap == tmap
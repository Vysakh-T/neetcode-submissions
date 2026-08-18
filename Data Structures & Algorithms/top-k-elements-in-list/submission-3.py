class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resMap = {}
        for i in nums:
            resMap[i] = resMap.get(i,0)+1
        tk = sorted(resMap.items(), key=lambda item: item[1], reverse=True)[:k]
        print(tk)
        return [i[0] for i in tk]
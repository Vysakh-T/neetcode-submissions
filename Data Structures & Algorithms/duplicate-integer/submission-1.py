class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrMap = dict()
        for i in nums:
            if arrMap.get(i):
                return True
            else:
                arrMap[i]=1
        return False
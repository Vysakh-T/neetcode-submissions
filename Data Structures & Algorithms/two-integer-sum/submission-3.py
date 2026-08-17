class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tdiff = {}
        for i in range(len(nums)):
            if nums[i] in tdiff:
                return [tdiff[nums[i]],i]
            diff = target - nums[i]
            tdiff[diff]=i
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[0]:
                return 0
            elif nums[i] >= target:
                return i
        return len(nums)
                
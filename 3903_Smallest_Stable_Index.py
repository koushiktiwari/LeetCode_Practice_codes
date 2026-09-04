class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            maxval = max(nums[0:i+1])
            minval = min(nums[i:len(nums)])
            if maxval - minval <= k:
                return i
        return -1

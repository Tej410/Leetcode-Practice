#longest consecutive sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_len = 0
        curr_len = 0
        for i in range(0,len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i] + 1:
                curr_len += 1
            else:
                curr_len = 0
            max_len = max(max_len,curr_len)
        return max_len+1

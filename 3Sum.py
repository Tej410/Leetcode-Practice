#three sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif sum < 0:
                    j+=1
                else:
                    k-=1
        return list(result)
         
        
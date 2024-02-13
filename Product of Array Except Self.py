#product of array except self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             prod*=nums[j]
        #     output.append(prod)
        # return output
        output=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
            
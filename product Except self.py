from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        dp=[1]*len(nums)
        for i in range (0,len(nums)):
            dp[i]= dp[i]*pre
            pre = pre*nums[i]
        print(dp)
        for i in range(len(nums) - 1, -1, -1): 
            dp[i] = dp[i] * post
            post = post * nums[i]
        return dp

sol = Solution()
print(sol.productExceptSelf([1,2,3,4,5]))
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        curr_max=curr_min=1
        res= max(nums)
        for i in nums:
            if(i==0):
                curr_max=1
                curr_min=1
                continue
            temp=curr_max*i
            curr_max=max(curr_max*i,curr_min*i,i)
            curr_min=min(temp,curr_min*i,i)
            res = max(curr_max,curr_min,res)
            print("curr_max is ", curr_max)
            print("curr_min is ", curr_min)
            print("res is ", res)
        return res
            
sol = Solution()
print(sol.maxProduct([-2,3,-4]))

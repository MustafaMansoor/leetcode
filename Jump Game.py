from typing import List
class Solution:
    def jump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            return 0
        if len(nums)==1:
            return 0
        l=0
        r=0
        farthest =0
        jumps=0
        while r < len(nums)-1:
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            
            jumps=jumps+1
            l=r+1
            r= farthest
        return jumps
            
            


sol = Solution()
temp = sol.jump([2,3,1,1,4])
print(temp)

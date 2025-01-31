from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        totalSum = sum(nums)
        
        for i in range(0,len(nums)):
            rightSum = totalSum - leftSum
            print(leftSum,rightSum)
            leftSum=leftSum+nums[i] 
            if(rightSum==leftSum):
                return i
                   
        return -1


sol = Solution()
print(sol.pivotIndex([2,1,-1]))
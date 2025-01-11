from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        forZero, forNonZero = 0, 0
        
        while forNonZero < len(nums):
            if nums[forNonZero] != 0:
                if forNonZero > forZero:
                    nums[forZero], nums[forNonZero] = nums[forNonZero], nums[forZero]
                forZero += 1
            forNonZero += 1
            
sol = Solution()
print(sol.moveZeroes([1,0,12,3,0 ,0]))
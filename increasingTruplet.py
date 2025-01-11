from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')

        for i in range(0,len(nums)):
            if nums[i] <= first:
                first=nums[i]
            elif nums[i]<= second:

                second = nums[i]
            else:
                return True
            print(first,second)
        return False




sol= Solution()
print(sol.increasingTriplet([2,1,5,0,4,6]))
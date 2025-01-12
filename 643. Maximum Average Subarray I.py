from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<k:
            return 0
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        
        max_sum = curr_sum
        
        left, right = 0, k
        while right < len(nums):
            new_sum = curr_sum - nums[left] + nums[right]
            if new_sum > max_sum:
                max_sum = new_sum
            curr_sum = new_sum
            left += 1
            right += 1
            
        return max_sum / k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
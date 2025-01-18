from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_count = 0
        curr_max = 0
        remaining_k = k
        
        while right < len(nums):
           
            if nums[right] == 1:
                curr_max += 1
                right += 1
            elif remaining_k > 0:
                curr_max += 1
                remaining_k -= 1
                right += 1
            else:
                if nums[left] == 0:
                    remaining_k += 1
                curr_max -= 1
                left += 1
                continue
                
            max_count = max(max_count, curr_max)
            
        return max_count

sol = Solution()
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
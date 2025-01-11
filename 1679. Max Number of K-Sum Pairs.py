from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        numMap = {} 
        
        for num in nums:
            target = k - num
            if target in numMap and numMap[target] > 0:
                count += 1
                numMap[target] -= 1
            else:
                numMap[num] = numMap.get(num, 0) + 1
        return count
sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))
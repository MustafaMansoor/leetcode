from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0]+gain
        for i in range(1,len(gain)):
            gain[i]= gain[i]+gain[i-1]
        return max(gain)

sol = Solution()

print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))

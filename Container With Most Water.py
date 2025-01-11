from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        res=0
        while left < right:
            area = (right-left) * min(height[left],height[right])
            res=max(res,area)
            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        return res
sol=Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])
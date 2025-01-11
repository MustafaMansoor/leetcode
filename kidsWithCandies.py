from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = max(candies)
        temp2= [False]*len(candies)
        for i in range (len(candies)):
            if extraCandies+candies[i] >= temp:
                temp2[i] = True
        return temp2
sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))
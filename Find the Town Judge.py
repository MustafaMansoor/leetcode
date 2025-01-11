from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dpin = [0]* n
        dpout = [0]* n 
        for src, des in trust:
            dpin[src-1] +=1
            dpout[des-1]+=1
      
        for i in range(0,n):
            if(dpin[i]==0 and dpout[i]==n-1):
                return i+1
        return -1
sol = Solution()
print(sol.findJudge(3,[[1,3],[2,3],[3,1]]))
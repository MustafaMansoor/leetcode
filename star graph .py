from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        Mydict = {}
        for src, des in edges:
            Mydict[src] = Mydict.get(src, 0) + 1
            Mydict[des] = Mydict.get(des, 0) + 1
        for key, value in Mydict.items():
            if value == len(Mydict)-1:
                return key
    
sol = Solution()
print(sol.findCenter([[1,2],[2,3],[4,2]]))
        
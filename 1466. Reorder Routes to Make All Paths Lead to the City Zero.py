from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        count=0
        for node in range (len(connections)):    
            if (self.haspath(connections, visited, node)==True):
                count+=1

    def haspath(self, connections, visited, room):
        if room in visited:
            return False
        visited.add(room)
        for oneroom in connections[room]:
            print(oneroom)
            self.haspath(connections, visited, oneroom)
        return True

sol = Solution()
print(sol.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))  

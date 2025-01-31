from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for i in range(len(isConnected)):    
            if i not in visited: 
                self.haspath(isConnected, visited, i)
                count += 1 
        return count
    def haspath(self, isConnected, visited, room):
        if room in visited:
            return
        visited.add(room)          
        for neighbor in range(len(isConnected[room])):  
            if isConnected[room][neighbor] == 1 and neighbor not in visited:
                self.haspath(isConnected, visited, neighbor)  
# print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  

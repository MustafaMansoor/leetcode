from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        return self.haspath(rooms, visited, 0)
        
    def haspath(self, rooms, visited, room):
        if room in visited:
            return False
        visited.add(room)
        for oneroom in rooms[room]:
            if self.haspath(rooms, visited, oneroom):
                return True
        return len(visited) == len(rooms)

sol =Solution()
print(sol.canVisitAllRooms([[1],[2],[3],[]]))
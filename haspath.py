from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def convertTOList():
            graph={}
            for edge in edges:
                [a,b]=edge
                # print(a,b)
                if(a not in graph):
                    graph[a]=[]
                if(b not in graph):
                    graph[b]=[]
                graph[a].append(b)
                graph[b].append(a)
            return graph
        graph = convertTOList()    
        visited=set()
        def checkPath(graph,src,dest,visited):
            if (src==dest): return True
            if(src in visited): return False
            visited.add(src)

            for node in graph[src]:
                if(checkPath(graph,node,dest,visited)==True):
                    return True
            return False
        return checkPath(graph,source,destination,visited)

        
sol = Solution()
print(sol.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5))
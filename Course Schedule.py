from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites = [p for p in prerequisites if p[0] < numCourses and p[1] < numCourses]

        graph,indeg = self.createList(prerequisites,numCourses)            
        # print(graph)
        queue=[]
        for i in range (0, len(indeg)):
            if(indeg[i]==0):
                queue.append(i)
        course_taken=0
        while(queue):
            course=queue.pop()
            course_taken+=1
            if(course in graph):
                for nodes in graph[course]:
                    
                    indeg[nodes]-=1
                    if indeg[nodes]==0:
                        queue.append(nodes)
        return numCourses==course_taken
    def createList(self,graph,num):
        adjlist ={}
        indeg = [0]*num
        for a1,b1 in graph:
            if(b1 not in adjlist):
                adjlist[b1]=[]
            adjlist[b1].append(a1)
            indeg[a1] += 1
        return adjlist,indeg
sol = Solution()

print(sol.canFinish(1, [[1,0]]))
        
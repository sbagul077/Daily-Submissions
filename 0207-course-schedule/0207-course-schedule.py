class Solution:
    path = []
    visited = []
    adj = {}
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = [False] * numCourses
        self.visited  = [False] * numCourses
        self.adj = {}
        
        for edge in prerequisites:
            if edge[1] not in self.adj:
                self.adj[edge[1]] = []
            self.adj[edge[1]].append(edge[0])
        
        for i in range(numCourses):
            if not self.visited[i] and self.hasCycle(i):
                return False
        
        return True
    
    def hasCycle(self, course):
        if self.path[course]:
            return True
        if self.visited[course]:
            return False
        
        self.visited[course] = True
        self.path[course] = True
        
        children = self.adj.get(course)
        
        if children:
            for i in children:
                if self.hasCycle(i):
                    return True
        
        self.path[course] = False
        return False
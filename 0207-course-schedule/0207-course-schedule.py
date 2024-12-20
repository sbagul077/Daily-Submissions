class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = dict()
                
        for curr in prerequisites:
            if curr[1] not in adj:
                adj[curr[1]] = []
            
            adj.get(curr[1]).append(curr[0])
            
            indegrees[curr[0]] += 1
        
        print(indegrees, adj)

        queue = deque()
        count = 0
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                count += 1
        
        while queue:
            curr = queue.popleft()
            temp = adj.get(curr)
            if temp:
                for i in temp:
                    indegrees[i] -= 1

                    if indegrees[i] == 0:
                        count += 1
                        queue.append(i)
        
        return count == numCourses
            
            
# 6
# [[2,0],[3,0],[1,2], [1,3],[4,2],[5,4],[5,3]]            
            
            
        
        
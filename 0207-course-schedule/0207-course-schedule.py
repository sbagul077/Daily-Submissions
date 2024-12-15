class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict()
        
        indegrees = [0] * numCourses
        
        for num in prerequisites:
            if num[1] not in adj.keys():
                adj[num[1]] = []
            
            adj[num[1]].append(num[0])
            
            indegrees[num[0]] += 1
            
        q = deque()
        count = 0
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1
        
        if len(q) == 0:
            return False
        
        while q:
            curr = q.popleft()
            li = adj.get(curr)
            if li:
                for node in li:
                    indegrees[node] -= 1

                    if indegrees[node] == 0:
                        q.append(node)
                        count += 1
        
        return count == numCourses
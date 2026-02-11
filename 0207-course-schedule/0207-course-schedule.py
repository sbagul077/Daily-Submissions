class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        adjList = [0 for i in range(numCourses)]
        hashMap = dict() 
        count = 0
        for course in prerequisites:
            adjList[course[0]] += 1

            if course[1] not in hashMap.keys():
                hashMap[course[1]] = []
            
            hashMap.get(course[1]).append(course[0])
        
        for i in range(len(adjList)):
            if adjList[i] == 0:
                queue.append(i)
                count += 1

        if len(queue) == 0:
            return False

        while len(queue) > 0:
            curr = queue.popleft()
            currList = hashMap.get(curr)
            # print(curr)
            if currList != None:
                for child in currList:
                    adjList[child] -= 1

                    if adjList[child] == 0:
                        queue.append(child)
                        count += 1
        
        if count == numCourses:
            return True
        
        return False


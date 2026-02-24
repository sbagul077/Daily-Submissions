"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        result = 0

        hashMap = dict()

        for emp in employees:
            hashMap[emp.id] = emp
        
        queue = deque()

        queue.append(id)

        while queue:
            currEmp = hashMap.get(queue.popleft())

            result += currEmp.importance

            for emp in currEmp.subordinates:
                queue.append(emp)
        
        return result


# //BFS
# // Time Complexity: O(N)
# // Space Complexity: O(N)

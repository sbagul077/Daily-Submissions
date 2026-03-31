# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    queue = []
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        self.insertIntoStack(nestedList)
        # print(self.queue)
    
    def insertIntoStack(self, integerList:[NestedInteger]):
        for element in integerList:
            if element.isInteger():
                self.queue.append(element.getInteger())
            else:
                self.insertIntoStack(element.getList())                
    
    def next(self) -> int:
        return self.queue.popleft()
        
    
    def hasNext(self) -> bool:
        if len(self.queue) > 0:
            return True
        
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
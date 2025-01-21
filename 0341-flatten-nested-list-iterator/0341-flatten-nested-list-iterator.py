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
    q = deque()
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque()        
        self.flatten(nestedList)

    def next(self) -> int:
        return self.q.popleft()
    
    def hasNext(self) -> bool:
        if len(self.q) > 0:
            return True
        return False
    
    def flatten(self, nestedList):
        print(nestedList)
        for ele in nestedList:
            if ele.isInteger():
                self.q.append(ele.getInteger())
            else:
                self.flatten(ele.getList())
        
        # for i in nestedList:
        #     if i.isInteger():
        #         self.queue.append(i.getInteger())
        #     else:
        #         self.fillQueue(i.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
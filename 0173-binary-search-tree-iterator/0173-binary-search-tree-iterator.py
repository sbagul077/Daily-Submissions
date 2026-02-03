# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ListNode:
    # val = None
    # next = None
    def __init__(self, val, next):
        self.val = val
        self.next = next

class BSTIterator:
    dummy = None
    head = None
    def __init__(self, root: Optional[TreeNode]):
        self.printroot = root
        self.head = ListNode(-1, None)
        self.dummy = self.head
        self.createLinkedList(root)
        # print(self.dummy.next)      
    
        # print(self.head.next.val)

    def next(self) -> int:
        self.head = self.head.next
        return self.head.val

    def hasNext(self) -> bool:
        if self.head.next:
            return True
        
        return False
    
    def createLinkedList(self, root):
        
        #base
        if root is None:
            return
        # print(root)
        self.createLinkedList(root.left)
        # print(root.val)
        node = ListNode(root.val, None)
        self.dummy.next = node
        # print( self.dummy.val, "before")
        self.dummy = self.dummy.next
        # print(self.dummy.val, "new dummy node")
        self.createLinkedList(root.right)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
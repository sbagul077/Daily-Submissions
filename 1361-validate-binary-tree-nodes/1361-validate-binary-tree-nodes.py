class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        arr = set(leftChild + rightChild)
        arr.discard(-1)
        
        if len(arr) == n:
            return False
        
        root = -1
        
        for i in range(n):
            if i not in arr:
                root = i
                break
        
        visited = set()
        
        def dfs(i):
            #base 
            if i == -1:
                return True
            
            if i in visited:
                return False
            
            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visited) == n
    
#DFS
#Time Complexity: O(n)
#Space Complexity: O(n)
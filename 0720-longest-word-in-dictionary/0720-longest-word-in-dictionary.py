class TrieNode:
    children = []
    isEnd = False
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Solution:
    result = ""
    root = None    
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:
        self.result = ""

        if words is None or len(words) == 0:
            return self.result

        for word in words:
            self.insert(word, self.root)
        
        self.dfs(self.root, [])

        return self.result

    def insert(self, word: str, root: TrieNode) -> None:
        curr = root

        for i in range(len(word)):
            char = word[i]
            if not curr.children[ord(char) - ord("a")]:
                curr.children[ord(char) - ord("a")] = TrieNode()
            
            curr = curr.children[ord(char) - ord("a")]
        
        curr.isEnd = True
    
    def dfs(self, curr, path):
        if len(path) >= len(self.result):
            self.result = "".join(path)
        
        for i in range(25, -1, -1):
            if curr.children[i] and curr.children[i].isEnd:
                le = len(path)
                #action
                path.append(chr(i + ord("a")))
                self.dfs(curr.children[i], path)
                path = path[: le]
        
  
#Time Complexity:; O(N * L), N is number of words, L is average word length.
#Space Compelxity: O(N * L)
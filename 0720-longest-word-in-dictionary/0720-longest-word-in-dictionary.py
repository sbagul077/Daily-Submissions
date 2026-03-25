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
        
        self.bfs(self.root)

        return self.result

    def insert(self, word: str, root: TrieNode) -> None:
        curr = root

        for i in range(len(word)):
            char = word[i]
            if not curr.children[ord(char) - ord("a")]:
                curr.children[ord(char) - ord("a")] = TrieNode()
            
            curr = curr.children[ord(char) - ord("a")]
        
        curr.isEnd = True
    
    def bfs(self, curr):
        currStr = ""
        queue = deque()
        strQ = deque()

        queue.append(curr)
        strQ.append(currStr)

        while queue:
            curr = queue.popleft()
            currStr = strQ.popleft()

            for i in range(25, -1, -1):
                if curr.children[i] and curr.children[i].isEnd:
                    queue.append(curr.children[i])
                    strQ.append(currStr + chr(i + ord("a")))

            self.result = currStr


#BFS
#Time Complexity:; O(N * L), N is number of words, L is average word length.
#Space Compelxity: O(N * L)
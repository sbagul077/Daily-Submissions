class TrieNode:
    
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for i in range(len(word)):
            char = word[i]
            if not curr.children[ord(char) - ord("a")]:
                curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(len(word)):
            char = word[i]
            if not curr.children[ord(char) - ord("a")]:
                return False
            curr = curr.children[ord(char) - ord("a")]
        
        return curr.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        
        for i in range(len(prefix)):
            char = prefix[i]
            
            if not curr.children[ord(char) - ord("a")]:
                return False
            curr = curr.children[ord(char) - ord("a")]
        
        return True
    
    
#Design 
#Time Complexity: O(L). Length of the word
#Space Complexity: O(n)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
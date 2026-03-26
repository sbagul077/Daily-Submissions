class TrieNode:
    children = []
    isEnd = False
    word = ""

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.word = ""

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # if len(sentence) == 0 or sentence is None or len(dictionary) == 0 or dictionary is None:
        #     return sentence
        
        sentence = sentence.split(" ")

        for word in dictionary:
            self.insert(word, self.root)
        
        result = []

        for j in range(len(sentence)):
            if j != 0:
                result.append(" ")

            word = sentence[j]
            replacement = []
            curr = self.root

            for i in range(len(word)):
                ch = word[i]
                
                if not curr.children[ord(ch) - ord("a")] or curr.isEnd:
                    break

                replacement.append(ch)
                curr = curr.children[ord(ch) - ord("a")]
                
            if curr.isEnd:
                result.append("".join(replacement))
            else:
                result.append(word)

        
        return "".join(result)                

    
    def insert(self, word: str, curr: TrieNode) -> None:
        print(word)
        for ch in word:
            if not curr.children[ord(ch) - ord("a")]:
                curr.children[ord(ch) - ord("a")] = TrieNode()
            
            curr = curr.children[ord(ch) - ord("a")]
        
        curr.isEnd = True
        curr.word = word


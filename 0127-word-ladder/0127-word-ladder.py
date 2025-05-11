class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        hashMap = dict()

        for i in range(len(wordList)):
            w = wordList[i]

            for j in range(len(w)):
                word = w[0:j] + "*" + w[j+ 1 : len(w)]
                # print(word)
                if word not in hashMap:
                    hashMap[word] =  list()
                hashMap[word].append(w)

        # print(hashMap)        
        queue = deque()
        queue.append(beginWord)

        visited = dict()
        visited[beginWord] = True
        level = 0
        while queue:
            size = len(queue)
            level += 1

            for i in range(size):
                word = queue.popleft()
                if word == endWord:
                    return level
                
                for j in range(len(word)):
                    newWord = word[0:j] + "*" + word[j+ 1: len(word)]
                    for adjWord in hashMap.get(newWord, []):
                        if adjWord not in visited.keys():
                            queue.append(adjWord) 
                            visited[adjWord]= True
        
        return 0



         

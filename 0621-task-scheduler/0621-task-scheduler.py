class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if tasks is None or len(tasks) == 0:
            return 0
        
        if n == 0:
            return len(tasks)
        
        hashMap = dict()
        maxFreq = 0

        for i in range(len(tasks)):
            char = tasks[i]
            if char not in hashMap.keys():
                hashMap[char] = 0
            
            hashMap[char] = hashMap.get(char) + 1
        
            maxFreq = max(maxFreq, hashMap.get(char))
        
        maxCount = 0

        for key, value in hashMap.items():
            if value == maxFreq:
                maxCount += 1
            
        partitions = maxFreq - 1
        empty = partitions * (n - (maxCount - 1))      
        pending = len(tasks) - (maxFreq * maxCount)
        idle = max(0, empty - pending)

        return len(tasks) + idle
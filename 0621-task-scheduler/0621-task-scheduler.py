class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = dict() 
        maxFreq = 0 # store the task with max count

        for i in range(len(tasks)):
            task = tasks[i]
            if task not in freqMap:
                freqMap[task] = 1
            else:
                freqMap[task] += 1

            maxFreq = max(maxFreq, freqMap.get(task))

        maxCount = 0        
        for key, value in freqMap.items():
            if maxFreq == value:
                maxCount += 1
        # print(maxCount, freqMap)   

        partition = maxFreq - 1
        # print(partition)
        empty = partition * (n - (maxCount - 1)) 
        # print(partition,empty)
        pending = len(tasks) - (maxFreq * maxCount)
        idle = max(0, empty - pending)

        return len(tasks) + idle

# Time Complexity: O(n)
# Space Complexity: O(1)
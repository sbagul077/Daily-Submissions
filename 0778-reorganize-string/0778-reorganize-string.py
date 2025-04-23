class Solution:
    def reorganizeString(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""

        freqMap = dict()

        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1

        maxHeap = [[-count, char] for char, count in freqMap.items()]

        heapq.heapify(maxHeap)
 
        prev = None
        result = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            top = heapq.heappop(maxHeap)
            count = top[0]
            char = top[1]


            result += char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
       
            if count != 0:
                prev = [count, char]
        

        return result

# Time Complexity : O(n log n) + O(n)
#Space Complexity:O(n)
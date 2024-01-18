from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        
        hashMap = dict()
        
        pq = PriorityQueue()
        
        for num in nums:
            if num not in hashMap.keys():
                hashMap[num] = 1
            else:
                hashMap[num] = hashMap.get(num) + 1
        
        # print(hashMap)
        for key in hashMap.keys():
            pq.put((hashMap.get(key), key))
            
            if pq.qsize() > k:
                pq.get()
        
        for i in range(k - 1, -1, -1):
            curr = pq.get()
            result[i] = curr[1]
        
        return result

#Dictionary, Min heap
#Time Complexity: O(nlogk)
#Space Complexity: O(n)
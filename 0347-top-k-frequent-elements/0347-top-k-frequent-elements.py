class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        hashMap = dict()
        max_num = float('-inf')
        
        for num in nums:
            if num not in hashMap.keys():
                hashMap[num] = 1
            else:
                hashMap[num] = hashMap.get(num) + 1
            
            max_num = max(max_num, hashMap.get(num))
        
        bucketArr = [None for i in range(max_num + 1)]
        
        for key, value in hashMap.items():
            if bucketArr[value]:
                bucketArr[value].append(key)
            else:
                bucketArr[value] = [key]
        
        for i in range(len(bucketArr) - 1, 0, -1):
            if k > 0:
                curr = bucketArr[i]                
                if bucketArr[i]:
                    for c in range(len(curr)):
                        if k > 0:
                            result.append(curr[c])
                            k -= 1
                        else:
                            break
            else:
                break
        # print(bucketArr, k)
        return result

#HashMap + BuckerArr
#Time Complexity: O(2n)
#Space Complexity: O(n)
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hashMap = defaultdict(list)

        for (t, user, web) in sorted(zip(timestamp, username, website)):
            print(t, user, web)
            hashMap[user].append(web)

        scores = defaultdict(int)

        for user, website in hashMap.items():
            for pattern in set(combinations(website, 3)):                
                scores[pattern] += 1
        
        maxPattern = ""
        maxCount = 0

        for pattern, cnt in scores.items():
            if cnt > maxCount or (cnt == maxCount and pattern < maxPattern):
                maxPattern = pattern
                maxCount = cnt
        
        return maxPattern
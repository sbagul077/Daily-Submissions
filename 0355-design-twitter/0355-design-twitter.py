from queue import PriorityQueue
class Tweets:
    def __init__(self,tweetId, time):
        self.id = tweetId
        self.time = time

class Twitter:
    tweets = dict()
    followed = dict()
    time = 0

    def __init__(self):
        self.time = 0
        self.tweets = dict()
        self.followed = dict()


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)

        if userId not in self.tweets:
            self.tweets[userId] = list()
        self.tweets[userId].append(Tweets(tweetId, self.time))
        self.time += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        fids = self.followed.get(userId)
        if fids:
            for fid in fids:
                tweetList = self.tweets.get(fid)
                if tweetList:
                    for tweet in tweetList:
                        heapq.heappush(pq, [tweet.time, tweet.id])
                        if len(pq) > 10:
                            heapq.heappop(pq)
        
        result = []
        print(pq)
        while pq:
            result.insert(0, heapq.heappop(pq)[1])
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followed.keys():
            self.followed[followerId] = set()

        self.followed[followerId].add(followeeId)            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]and followerId != followeeId:
            self.followed.get(followerId).remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
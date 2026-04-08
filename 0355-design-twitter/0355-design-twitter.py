import heapq

class Tweet:

    def __init__(self, time, tweetId):
        self.createdAt = time
        self.tweetId = tweetId
class Twitter:
    time = 0
    tweets = dict()
    followed = dict()

    def __init__(self):
        self.time = 0
        self.tweets = dict()
        self.followed = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)

        if userId not in self.tweets.keys():
            self.tweets[userId] = list()
        
        self.tweets[userId].append(Tweet(self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hq = []

        fIds = self.followed.get(userId)

        if fIds:
            for fId in fIds:
                fTweets = self.tweets.get(fId)
                if fTweets:
                    for tweet in fTweets:
                        hq.append([tweet.createdAt, tweet.tweetId])
                        heapify(hq)

                        if len(hq) > 10:
                            heapq.heappop(hq)
        
        # print(hq)
        result= []
        while len(hq) > 0:
            result.insert(0, heapq.heappop(hq)[1])
        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followed.keys():
            self.followed[followerId] = set()

        self.followed[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.followed.keys() and followeeId in self.followed[followerId] and followerId != followeeId:
            self.followed.get(followerId).remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
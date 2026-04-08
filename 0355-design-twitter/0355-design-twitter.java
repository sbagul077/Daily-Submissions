class Tweets{
    int createdAt;
    int tweetId;

    public Tweets(int time, int tweetId){
        this.createdAt = time;
        this.tweetId = tweetId;
    }
}
class Twitter {
    int time;
    HashMap<Integer, List<Tweets>> tweetsPosted;
    HashMap<Integer, HashSet<Integer>> followed;

    public Twitter() {
        this.time = 0;
        this.tweetsPosted = new HashMap<>();
        this.followed = new HashMap<>();        
    }
    
    public void postTweet(int userId, int tweetId) {
        follow(userId, userId);
        if(!tweetsPosted.containsKey(userId)){
            tweetsPosted.put(userId, new ArrayList<>());
        }

        tweetsPosted.get(userId).add(new Tweets(time, tweetId));
        time++;       
        // tweetsPosted.forEach((key, value) -> System.out.println(key + " : " + value));

    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweets> pq = new PriorityQueue<>((a, b) -> a.createdAt - b.createdAt);

        HashSet<Integer> fIds = followed.get(userId);
    
        if(fIds != null){
            for(int fId: fIds){
                // System.out.println(fId);
                List<Tweets> tweetList = tweetsPosted.get(fId);
                // System.out.println(tweetList);
                if(tweetList != null){
                    for(Tweets tweet: tweetList){
                        pq.add(tweet);
                        if(pq.size() > 10){
                            pq.poll();
                        }
                    }
                }
            }
        }

        List<Integer> feed = new ArrayList<>();
        while(!pq.isEmpty()){
            feed.add(0,pq.poll().tweetId);
        }

        return feed;

    }
    
    public void follow(int followerId, int followeeId) {
        if(!followed.containsKey(followerId)){
            followed.put(followerId, new HashSet<>());
        }
        followed.get(followerId).add(followeeId);     
    }
    
    public void unfollow(int followerId, int followeeId) {
        if(followed.containsKey(followerId) && followed.get(followerId).contains(followeeId) && followerId != followeeId){
            followed.get(followerId).remove(followeeId);
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
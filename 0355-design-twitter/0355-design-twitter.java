class Twitter {
    class Tweets{
        int id;
        int createdAt;
        public Tweets(int tweetId, int time){
            this.id = tweetId;
            this.createdAt = time;
        }
    }
    public int time;
    public HashMap<Integer, List<Tweets>> tweets;
    public HashMap<Integer, HashSet<Integer>> followed;

    public Twitter() {
        tweets = new HashMap<>();
        followed = new HashMap<>();        
        time = 0;
    }
    
    public void postTweet(int userId, int tweetId) {
        //entries in followed table and tweets table
        follow(userId, userId);
        if(!tweets.containsKey(userId)){
            tweets.put(userId, new ArrayList<>());
        }
        // Tweets newTweet = new Tweets(tweetId, time++);

        tweets.get(userId).add(new Tweets(tweetId, time++));
    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweets> pq = new PriorityQueue<>((a, b) -> a.createdAt- b.createdAt);
        //get list of people userId is following
        HashSet<Integer> fids = followed.get(userId);
        if(fids != null){
            for(int fid : fids){
                List<Tweets> tweetList = tweets.get(fid);
                if(tweetList != null){
                    for(Tweets tweet: tweetList){
                        pq.add(tweet);
                        if(pq.size()> 10){
                            pq.poll();
                        }
                    }
                }
            }
        }
        List<Integer> feed = new ArrayList<>();
        while(!pq.isEmpty()){
            feed.add(0, pq.poll().id);
        }
        // System.out.println(feed);
        return feed;

    }
    
    public void follow(int followerId, int followeeId) {
        if(!followed.containsKey(followerId)){
            followed.put(followerId, new HashSet<>());
        }
        followed.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if(followed.containsKey(followerId) && followerId != followeeId){
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
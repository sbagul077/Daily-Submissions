class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.bucketItems = 1000
        self.storage = [False for i in range(self.buckets)]   
 
    def getbucket(self, key):
        return key % self.buckets
    
    def getbucketItem(self, key):
        return key // self.bucketItems 
    
    def add(self, key: int) -> None:
        bucket = self.getbucket(key)
        bucketItem = self.getbucketItem(key)

        if self.storage[bucket] == False:
            self.storage[bucket] = [False] * 1000
            if bucket == 0:
                # self.storage[bucket] = [False] * (self.bucketItems + 1)                
                self.storage[bucket].append(False)
            # else:
            #     self.storage[bucket] = []*self.bucketItems
        # print(bucketItem, bucket)        
        self.storage[bucket][bucketItem] =  True
                   

    def remove(self, key: int) -> None:
        bucket = self.getbucket(key)
        bucketItem = self.getbucketItem(key)
        
        if self.storage[bucket] == False:
            return
        
        self.storage[bucket][bucketItem] = False

    def contains(self, key: int) -> bool:
        bucket = self.getbucket(key)
        bucketItem = self.getbucketItem(key)
        
        if self.storage[bucket] == False:
            return False
        
        return self.storage[bucket][bucketItem]
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
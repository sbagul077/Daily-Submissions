class MyHashSet:

    bucket = 0;
    bucketItems = 0;
    storage = []

    def __init__(self):
        self.bucket = 1000;
        self.bucketItems = 1000;
        self.storage = [None] * self.bucket

    def getBucket(self, key):
        return key % 1000;
    
    def getBucketItems(self, key):
        return key // 1000;

    def add(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)
        # print(bucket,self.storage)
        if(self.storage[bucket] is None):
            if bucket == 0:
                self.storage[bucket] = [False] * (self.bucketItems + 1)
            else:
                self.storage[bucket] = [False] * self.bucketItems

        self.storage[bucket][bucketItem] = True               

    def remove(self, key: int) -> None:
        
        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)

        if(self.storage[bucket] is not None):
            self.storage[bucket][bucketItem] = False        

    def contains(self, key: int) -> bool:

        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)

        if(self.storage[bucket]):
            # print(bucketItem,self.storage[bucket])
            if(self.storage[bucket][bucketItem]):
                return True
        
        return False


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.hashMap = dict()
        self.queue = deque()

        for i in range(maxNumbers):
            self.hashMap[i] = True
            self.queue.append(i)

    def get(self) -> int:
        if len(self.queue) > 0:
            slot = self.queue.popleft()
            self.hashMap[slot] = False
            return slot
        return -1        

    def check(self, number: int) -> bool:
        return self.hashMap.get(number)

    def release(self, number: int) -> None:
        if not self.hashMap.get(number):
            self.hashMap[number] = True
            self.queue.append(number)
        
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
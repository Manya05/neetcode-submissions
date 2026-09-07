class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.nums_index={}

    def insert(self, val: int) -> bool:
        if val in self.nums_index:
            return False
        self.nums.append(val)
        self.nums_index[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_index:
            return False
        idx = self.nums_index[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.nums_index[last] = idx

        self.nums.pop()
        del self.nums_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.nums.append(val)
        self.indices[val] = len(self.nums) - 1
        print(self.nums, self.indices)
        return True
        # hash function: f(val)=current len(nums)

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        print(self.nums, self.indices)
        return True

    def getRandom(self) -> int:
        from random import choice

        return choice(self.nums)


o1 = RandomizedSet()
o1.insert(1)
o1.insert(2)
o1.insert(3)
o1.remove(3)
o1.getRandom()

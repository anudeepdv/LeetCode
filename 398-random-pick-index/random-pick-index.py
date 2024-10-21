class Solution:

    def __init__(self, nums: List[int]):
        self.map = collections.defaultdict(list)
        for i,val in enumerate(nums):
            self.map[val].append(i)


    def pick(self, target: int) -> int:
        l = len(self.map[target])

        rand = randint(0, l-1)

        print(l,rand)

        return self.map[target][rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
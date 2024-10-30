class Solution:

    def __init__(self, nums: List[int]):

        self.d=collections.defaultdict(list)

        for i ,val in enumerate(nums):
            self.d[val].append(i)
        
    def pick(self, target: int) -> int:
        targetList = self.d[target]
        l=0
        r=len(targetList)-1

        return self.d[target][random.randint(l, r)]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
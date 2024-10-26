class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        

        res=[-1]*len(nums)

        q =deque()

        n = len(nums)
        for i in range(0,len(nums)*2):
            while q and nums[i%n]>nums[q[-1]]:
                pop = q.pop()
                res[pop] = nums[i%n]

            q.append(i%n)

        return res

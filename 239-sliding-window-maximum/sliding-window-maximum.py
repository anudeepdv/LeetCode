class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l=0
        r=0

        q=collections.deque()
        res=[]
        for r in range(len(nums)):
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            
            q.append(r)
            # print(q)
            if r-k ==q[0]:
                q.popleft()
            if r+1>=k:
                res.append(nums[q[0]])

        return res
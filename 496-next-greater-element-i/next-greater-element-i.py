class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res=[-1]*len(nums1)

        q= deque()

        d={}
        for i,val in enumerate(nums1):
            d[val]=i

        for i in nums2:
            while q and i>q[-1]:
                pop = q.pop()
                res[d[pop]]=i

            if i in d:
                q.append(i)

        return res


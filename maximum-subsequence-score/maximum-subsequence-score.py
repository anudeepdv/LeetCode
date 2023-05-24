class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:


        h = []

        heapq.heapify(h)

        l = [(n1,n2) for n1,n2 in zip(nums1,nums2)]

        l=sorted(l,key= lambda x : x[1], reverse=True)

        res=0
        nums=0
        for n1,n2 in l:
            nums=nums+n1
            heapq.heappush(h,n1)
            if len(h)>k:
                pop = heapq.heappop(h)
                nums=nums-pop
            
            if(len(h)==k):
                res=max(res,nums*n2)

        return res

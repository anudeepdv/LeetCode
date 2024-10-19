class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1

        a = Counter(nums1)
        b= Counter(nums2)
        res=[]
        for i in a:
            if i in b:
                for _ in range(min(a[i],b[i])):
                    res.append(i)

        return res


        
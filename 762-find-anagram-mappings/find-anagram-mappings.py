class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d={}

        for i in range(len(nums2)):
            d[nums2[i]]=i
            

        res=[]
        for  i in nums1:
            res.append(d[i])

        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n1=[1 for i in range(len(nums))]
        k=1
        for i in range(len(nums)-1):
            n1[k]=n1[k-1]*nums[i]
            k=k+1
        # print(n1)

        n2=[1 for i in range(len(nums))]
        k=len(nums)-2
        for i in range(len(nums)-1,0,-1):
            n2[k]=n2[k+1]*nums[i]
            k=k-1

        # print(n2)

        n3=[1 for i in range(len(nums))]

        for i in range(len(nums)):
            n3[i]=n1[i]*n2[i]

        return n3

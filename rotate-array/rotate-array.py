class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        while k>0:
            pop=nums.pop()
            nums.insert(0,pop)
            k=k-1
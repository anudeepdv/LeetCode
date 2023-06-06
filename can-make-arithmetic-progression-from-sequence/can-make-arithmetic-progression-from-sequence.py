class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        diff = arr[1]-arr[0]
        prev= arr[1]
        for i in arr[2:]:
            diff2= i-prev
            if diff2 != diff:
                return False
            prev=i
        
        return True
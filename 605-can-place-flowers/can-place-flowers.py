class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            left = 0 if i-1<0 else flowerbed[i-1]
            right = 0 if i+1>=len(flowerbed) else flowerbed[i+1]

            cur = flowerbed[i]

            if left ==0 and right ==0 and cur==0:
                n-=1
                flowerbed[i]=1

        return True if n<=0 else False
            
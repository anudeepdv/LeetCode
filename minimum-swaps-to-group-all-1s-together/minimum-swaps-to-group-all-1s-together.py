class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones=0
        for i in data:
            if i==1:
                ones+=1

        n=len(data)
        curOnes=0
        for i in range(ones):
            if data[i]==1:
                curOnes=curOnes+1
        minSwaps = ones-curOnes
     
        for i in range(1,n-ones+1):
            if data[i-1]==1:
                curOnes-=1
            if data[i+ones-1]==1:
                curOnes+=1

            minSwaps=min(minSwaps, ones-curOnes)

        return minSwaps
            

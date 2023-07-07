class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        arr= [0]*length
        for i in updates:
            arr[i[0]]+=i[2]
            if i[1]+1<length:
                arr[i[1]+1]-=i[2]

        for i in range(1,length):
            arr[i]=arr[i]+arr[i-1]

        return arr
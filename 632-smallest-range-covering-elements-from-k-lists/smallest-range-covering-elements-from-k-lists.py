class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        heapArray=[]
        hashMap ={}
        maxVal =nums[0][0]
        for i in range(len(nums)):
            heapArray.append((nums[i][0],i))
            hashMap[i]=nums[i]
            if(nums[i][0]>maxVal):
                maxVal=nums[i][0]
        heapq.heapify(heapArray)

        isEmpty=False
        minRange =100000000
        rangeCombo =[]
        while(isEmpty!=True):
            element, i = heapq.heappop(heapArray)
            if(maxVal-element)<minRange:
                minRange=maxVal-element
                rangeCombo=[element,maxVal]
            listRet=hashMap[i]
            if(len(listRet)==0):
                break
            newElement=listRet.pop(0)
            maxVal=max(maxVal,newElement)
            
            
           
            heapq.heappush(heapArray, (newElement, i))
            

        return rangeCombo


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if(len(hand)%groupSize!=0):
            return False

        hashMap = collections.Counter(hand)

        h=list(hashMap.keys())

        heapq.heapify(h)

        while h:
            first =h[0]
            for i in range(first,first+groupSize):
            
                if i in hashMap:
                    if hashMap[i]>0:
                        hashMap[i]=hashMap[i]-1
                    
                    if hashMap[i]==0:
                        if h[0]!=i:
                            return False
                        else:
                            heapq.heappop(h)
                else:
                    return False
                
        return True



      


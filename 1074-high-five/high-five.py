class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        
        heapdict=collections.defaultdict(list)
        for i in items:
            if i[0] in heapdict:
                heapdict[i[0]].append(-i[1])
            else:
                heapdict[i[0]]=[-i[1]]
        l=[]
        print(heapdict)
        for i in heapdict:
            heapq.heapify(heapdict[i])
            res=0
            k=5
            while k>0:
                res+= -heapq.heappop(heapdict[i])
                k-=1

            l.append([i,res//5])

        l.sort(key=lambda x:x[0])
        return l
            


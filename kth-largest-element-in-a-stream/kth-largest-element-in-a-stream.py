class KthLargest:

   
    
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapify(self.heap)
        self.k=k
        for i in nums:

            if len(self.heap) ==k and self.heap[0]<i:
                heappop(self.heap)
                heappush(self.heap,i)
               
            elif len(self.heap) <k:
                heappush(self.heap,i)
        
        

    def add(self, val: int) -> int:
        # print(self.heap)
      
        if  len(self.heap)<self.k:
            heappush(self.heap,val)
        elif  self.heap[0]<val:
            heappop(self.heap)
            heappush(self.heap,val)
       
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
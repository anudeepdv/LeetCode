class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        q=collections.deque()
        q.append(0)
        s=0
        vis=set()
        vis.add(0)
        while q:
            print(q)
            for i in range(len(q)):
                cur=q.popleft()
                for k in range(nums[cur]+1):
                    if cur+k not in vis:
                        if cur+k==len(nums)-1:
                            return s+1
                        q.append(cur+k)
                        vis.add(cur+k)

            s+=1

        return 0


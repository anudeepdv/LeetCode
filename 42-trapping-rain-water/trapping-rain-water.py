class Solution:
    def trap(self, height: List[int]) -> int:
       
        l=[0]
        curleft =height[0]

        for i in range(1,len(height)):
            l.append(curleft)
            curleft=max(curleft,height[i])

        print(l)

        r=[0]
        curright = height[-1]
        for i in range(len(height)-2,-1,-1):
            r.insert(0,curright)
            curright=max(curright,height[i])

        print(r)

        res=0

        for i in range(len(height)):
            val = min(l[i],r[i])-height[i]
            if val>0:
                res=res+val
        return res
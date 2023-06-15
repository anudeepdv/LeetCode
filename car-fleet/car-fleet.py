class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[]
        for i in zip(position,speed):
            res.append(i)

        res=sorted(res,key=lambda x:x[0],reverse=True)

        print(res)
        stack=[]

        for i in res:
            a=(target-i[0])/i[1]
            stack.append(a)
            # print(stack)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
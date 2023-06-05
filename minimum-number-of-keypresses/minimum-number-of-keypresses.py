class Solution:
    def minimumKeypresses(self, s: str) -> int:

        hashMap = collections.defaultdict(int)

        for i in s:
            hashMap[i]=hashMap[i]+1

        calls=[]
        for i in hashMap:
            calls.append((i,hashMap[i]))

        calls = sorted(calls,key=lambda x:x[1],reverse=True)
        c=1

        callMap={}
        for i in calls:
            callMap[i[0]]=math.ceil(c/9)
            c=c+1

        print(callMap)
        res=0
        for i in s:
            res=res+callMap[i]


        return res





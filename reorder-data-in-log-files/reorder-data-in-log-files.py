class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digitLogs=[]

        alphaLogs=[]

        for i in logs:
            if i[-1].isdigit():
                digitLogs.append(i)

            else:
                alphaLogs.append(i)

        res=[]
        print(digitLogs)

        alphaLogs= sorted(alphaLogs,key=lambda x : (x.split(' ')[1:],x.split(' ')[0]))

        

        return alphaLogs+digitLogs

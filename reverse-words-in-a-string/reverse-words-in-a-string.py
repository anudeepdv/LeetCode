class Solution:
    def reverseWords(self, s: str) -> str:

        i=0

        while s[i]==' ':
            i=i+1
        
        j=len(s)-1

        while s[j]==' ':
            j=j-1

        # print(i,j)
    
        s=s[i:j+1]

        eod=False
        res=[]
        start=''
        for i in s:
            
            if i==' ' and eod:
                # print('x')
                continue
            elif i==' ':
                # print(start)
                res.insert(0,start)
                start=''
                eod=True
            else:
                # print(i)
                eod=False
                start=start+i

        if start!='':
            res.insert(0,start)
       
        # print(res)

        return ' '.join(res)



class Solution:
    def compress(self, chars: List[str]) -> int:
        
        r= 0 

        s=''
        i=0
        while  r<len(chars):

            l=r
            cur = chars[r]
            while r<len(chars) and  cur ==chars[r]:
                r+=1
            if r-l==1:
                chars[i]=cur
                i+=1
            else:
                chars[i]=cur
                i+=1
                for j in str(r-l):
                    chars[i]=j
                    i+=1
            print(cur,r-l)
       
        return i
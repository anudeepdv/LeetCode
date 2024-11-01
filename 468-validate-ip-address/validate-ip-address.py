class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def valipv4(queryIP):
            l = queryIP.split(".")

            for num in l:
                if len(num) == 0  or (len(num)>1 and num[0]=='0') or not num.isnumeric() or int(num)>255:
                    print(num)
                    return "Neither"
            
            return "IPv4"

        def valipv6(queryIP):
            l = queryIP.split(':')

            for num in l:
                print(num)
                if len(num)==0 or len(num)>4:
                    return "Neither"
     
                for i in num:
         
                    if not(ord(i) in range(97,103) or ord(i) in range(65,71) or  ord(i) in range(48,58)):
                        return "Neither"

                

            
            return "IPv6"
        
       
        
        if queryIP.count('.')==3:
            return valipv4(queryIP)

        elif queryIP.count(':')==7:
   
            return valipv6(queryIP)
        else:
            return "Neither"


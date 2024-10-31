class Solution:
    def decodeString(self, s: str) -> str:
        #Time - O(N) Space - O(MAX Num * str )
        q =[]

        for i in s:
            # print(q)
            if i!=']':
                q.append(i)
            elif i ==']':
                
                chars = ""
                while q[-1]!='[':
                    chars=q.pop()+chars
                # print(chars)
                if q[-1]=='[':
                    q.pop()
                # print(q)
                num=""
                while q and q[-1].isdigit():
                    # print(q)
                    num+=q.pop()
                    # print(num,"Num")
                num = int(num[::-1])
                q.append(chars*num)
                # print(q)

        return ''.join(q)
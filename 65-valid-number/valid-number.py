class Solution:
    def isNumber(self, s: str) -> bool:
        
        dot=exponent=decimal = False
        seen=False

        for i,val in enumerate(s):
            if val in "Ee":
                if not seen:
                    return False
                if exponent:
                    return False
                exponent=True
                seen=False
            elif val=='.':
                if exponent:
                    return False
                print("hi",decimal)
                if decimal:
                    return False
                decimal=True
            elif val in '+-':
                
                if not(i==0 or s[i-1] in "Ee"):
                    print('Yo')
                    return False
            elif s[i].isdigit():
                seen=True
            else:
                return False

        return seen

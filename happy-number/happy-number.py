class Solution:
    def isHappy(self, n: int) -> bool:

        vis = set()

        while n not in vis:

            a=str(n)
            val=0
            for i in a:
                val = val+int(i)*int(i)

            if(val==1):
                return True
            vis.add(n)
            n=val

        return False


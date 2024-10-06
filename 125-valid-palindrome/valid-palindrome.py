class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(ord('a'))
        print(ord('z'))
        print(ord('A'))
        print(ord('Z'))
        print(ord("0"))
        print(ord("9"))

       
        a=''
        for i in s:
            if ord(i) in range(97,123) or ord(i) in range(65,91) or ord(i) in range(48,58):
                a=a+i.lower()
        print(a)
        
        l =0 
        r= len(a)-1

        while l<=r:
            if a[l]!=a[r]:
                return False
            l=l+1
            r=r-1
        return True
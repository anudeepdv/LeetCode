class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # print(ord("a"),ord("z"),ord("z")-ord("a"))
        s1_list =[0]*26

        for i in s1:
            s1_list[ord(i)-ord('a')]+=1
        # print(s1_list)
        k=len(s1)
        l=0
        s2_list=[0]*26
        for r in range(len(s2)):
            if r<k:
                # print(s2[r])
                s2_list[ord(s2[r])-ord('a')]+=1
                if r-l+1==k:
                    # print(s2[l:r+1])
                    if tuple(s2_list)==tuple(s1_list):
                        return True

            else:
                s2_list[ord(s2[r])-ord('a')]+=1
                s2_list[ord(s2[l])-ord('a')]-=1
                l+=1   
                if tuple(s2_list)==tuple(s1_list):
                        return True       
                # print(s2[l:r+1])


        return False



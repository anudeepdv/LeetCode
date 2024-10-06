class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        n = len(s)

        wordlen = len(words[0])
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        res= []
        for i in range(n - (len(words)*wordlen)+1):
            temp = collections.defaultdict(int)
            # print(temp)
            for j in range(i, i+wordlen*len(words),wordlen):
                # print(s[j:j+wordlen])
                word = s[j:j+wordlen]
                if word in d:
                    temp[word]+=1
                    if temp[word] >d[word]:
                        break
                else:
                    break
            else:
                res.append(i)
                    
            
            

        return res

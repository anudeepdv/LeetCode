class Solution:
    def isValid(self, s: str) -> bool:
        q=collections.deque()

        d={'(':')','{':'}','[':']'}

        for i in s:
            if i in d:
                q.append(i)
            else:
                if len(q)==0:
                    return False
                p = q.pop()
                if d[p] == i:
                    continue
                else:
                    return False

        if len(q)==0:
            return True
        else:
            return False
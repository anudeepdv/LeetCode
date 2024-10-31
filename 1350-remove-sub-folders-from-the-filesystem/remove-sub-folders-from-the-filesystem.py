class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort()
        seen = [folder[0]]

        for i in folder[1:]:
            if i.startswith(seen[-1]+'/'):
                continue
            else:
                seen.append(i)

        return seen
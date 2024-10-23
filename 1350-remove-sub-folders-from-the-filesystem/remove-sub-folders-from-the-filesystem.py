class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        seen = [folder[0]]

        for i in range(1,len(folder)):
            if folder[i].startswith(seen[-1]+'/'):
                continue
            else:
                seen.append(folder[i])

        return seen
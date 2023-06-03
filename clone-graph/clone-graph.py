"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return
        hashMap={}
        q=collections.deque([node])

        while(q):
            print(q)
            curNode = q.popleft()
            # print(curNode.val)
            if curNode not in hashMap:
                hashMap[curNode]=Node(curNode.val,[])
            
            for nei in curNode.neighbors:
                if nei not in hashMap:
                    CopNei=Node(nei.val,[])
                    hashMap[nei]=CopNei
                    print(nei.val)
                    q.append(nei)
                    hashMap[curNode].neighbors.append(CopNei)
                else:
                    hashMap[curNode].neighbors.append(hashMap[nei])

        return hashMap[node]

